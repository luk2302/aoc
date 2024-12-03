// ==UserScript==
// @name         AOC custom score board
// @namespace    https://github.com/luk2302/aoc/blob/master/custom_leaderboard_userscript.js
// @version      0.1
// @description  AOC custom score board
// @author       Lukas Rinke
// @match        https://adventofcode.com/*/leaderboard/private/view/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=adventofcode.com
// @grant        none
// ==/UserScript==

/*

This is a userscript that can be used, e.g. via Tampermonkey in your browser.

The userscript applies to any private leaderboard, for all events / years and adds a coupld of things:
* sorting options, you can sort the leaderboard by
** the actual score
** the solution times for the first star
** the solution times for the second star
** the difference between the solution times for first and second star
* ability to display and sort previous days instead of just showing the current day
* highlighting to your own row
* (only visual) removal of inactive users

 */

(function() {
    'use strict';

    let parts = document.location.href.split("/")
    fetch(`${parts[parts.length - 1]}.json`).then(function(response) {
        return response.json();
    }).then(function(data) {
        customizeScoreboard(data);
    });
})();

let players = []
let year = parseInt(document.location.href.split("/")[3])

function customizeScoreboard(scoreboardData) {
    let members = Object.keys(scoreboardData.members).map(function (id) {
        return {...scoreboardData.members[id], id};
    });

    members = members.filter(member => member.local_score !== 0)
    members.sort((a, b) => b.local_score - a.local_score)

    let now = new Date()
    let dayToCheck = now.getUTCHours() < 5 ? now.getUTCDate() - 1 : now.getUTCDate()
    if (year < now.getUTCFullYear() || dayToCheck > 25) {
        dayToCheck = 25
    }

    function showTime(day, time) {
        function pad(n) {
            return String(n).padStart(2, "0")
        }

        if (time === undefined) {
            return "-"
        }
        let off = time - day
        let m = Math.floor(off / 60)
        let s = off % 60
        if (m < 60) {
            return `${pad(m)}:${pad(s)}`
        } else {
            return `${Math.floor(m / 60)}:${pad(m % 60)}:${pad(s)}`
        }
    }

    players = members.map(function (member) {
        let days = []
        for (let day = 0; day < dayToCheck; day++) {
            let startOfAocDayTs = new Date(Date.UTC(year, 11, day + 1, 5)).getTime() / 1000
            let firstStar = member.completion_day_level[String(day + 1)]?.["1"]?.get_star_ts
            let secondStar = member.completion_day_level[String(day + 1)]?.["2"]?.get_star_ts
            let dailyTimesStr = `* (${showTime(startOfAocDayTs, firstStar)} / ${showTime(startOfAocDayTs, secondStar)}) `
            days.push({
                "local_score": 0,
                "local_score_original": member.local_score,
                "daily_times_str": dailyTimesStr,
                "first_star": firstStar,
                "second_star": secondStar,
                "name": member.name,
            })
        }
        return {
            "name": member.name,
            "id": member.id,
            "days": days,
        }
    })

    let htmlObjects = getScoreboardRows()
    // remove inactive users
    for (let i = players.length; i < htmlObjects.length; i++) {
        htmlObjects[i].remove()
    }
    // highlight current player
    let thisPlayer = document.getElementsByClassName("user")[0].childNodes[0].textContent.trim()
    let matchingPlayers = players.filter(player => player.name === thisPlayer)
    for (let i = 0; i < players.length; i++) {
        htmlObjects[i].dataset.playerIndex = String(i)
        if (matchingPlayers.length === 1 && htmlObjects[i].getElementsByClassName("privboard-name")[0].childNodes[0].textContent.trim() === thisPlayer) {
            htmlObjects[i].classList.add("currentUser")
        }
        if (!htmlObjects[i].children[0].classList.contains('privboard-position')) {
            let posElement = document.createElement("span")
            posElement.classList.add('privboard-position')
            htmlObjects[i].insertBefore(posElement, htmlObjects[i].firstChild)
        }
    }
    deduplicateUsernames(players)
    computeScores(htmlObjects.length)
    setScoreboardAttributes(dayToCheck)
    setupSorting()
    setupDaySelection(dayToCheck)
    createCss()
}

function deduplicateUsernames(players) {
    let names = new Set()
    let duplicates = []
    for (let i = 0; i < players.length; i++) {
        let name = players[i].name
        if (name === null) {
            continue
        }
        if (names.has(name)) {
            duplicates.push(name)
        } else {
            names.add(name)
        }
    }
    let html = getScoreboardRows()
    duplicates.forEach(duplicate => {
        for (let i = 0; i < players.length; i++) {
            let name = players[i].name
            let id = players[i].id
            if (name === duplicate) {
                html[i].lastChild.childNodes[0].textContent = `${name} ${id} `
            }
        }
    })
}

function computeScores(numUnfilteredPlayers) {
    function compute(attribute, day) {
        const sortedFirst = [...players].sort((a, b) => {
            if (a.days[day][attribute] === undefined) {
                return 1
            }
            if (b.days[day][attribute] === undefined) {
                return -1
            }
            return a.days[day][attribute] - b.days[day][attribute]
        });
        for (let playersBefore = 0; playersBefore < sortedFirst.length; playersBefore++) {
            let gained = numUnfilteredPlayers - playersBefore
            if (sortedFirst[playersBefore].days[day][attribute] !== undefined) {
                sortedFirst[playersBefore].days[day].local_score += gained
            }
        }
    }
    for (let day = 0; day < players[0].days.length; day++) {
        if (day > 0) {
            for (let i = 0; i < players.length; i++) {
                players[i].days[day].local_score = players[i].days[day - 1].local_score
            }
        }
        compute("first_star", day)
        compute("second_star", day)
    }
}

function toggleClass(cls, ele) {
    [].forEach.call(document.getElementsByClassName(cls), function(el) {
        el.classList.remove(cls);
    });
    ele.classList.add(cls)
}

function setupDaySelection(days) {
    let dayElements = document.getElementsByClassName("privboard-days")[0].children
    for (let day = 0; day < days; day++) {
        dayElements[day].dataset.day = String(day)
        dayElements[day].addEventListener("click", selectDay)
    }
    dayElements[days - 1].classList.add("activeDay")
}

function selectDay(e) {
    if (e.target.classList.contains("activeDay")) {
        return
    }

    toggleClass("activeDay", e.target)
    let day = parseInt(e.target.dataset.day) + 1
    setScoreboardAttributes(day)
    document.getElementsByClassName("activeSort")[0].click()

    e.preventDefault()
    return false
}

function createCss() {
    let css = '.activeSort { color: lightgreen; } .activeDay { color: lightgreen; } .currentUser { color: red; } .currentUser a { color: red; }'
    let style = document.createElement('style')
    document.head.appendChild(style);
    style.appendChild(document.createTextNode(css));
}

function getScoreboardRows() {
    let htmlObjects = [...document.getElementsByClassName("privboard-row")]
    htmlObjects.shift()
    return htmlObjects
}

let lastSelectedDay = 0
function setScoreboardAttributes(day) {
    let d = day - 1
    let htmlObjects = getScoreboardRows()
    let maximumTimesLength = 0;
    let maximumScoreLength = 0;
    for (let i = 0; i < players.length; i++) {
        maximumTimesLength = Math.max(maximumTimesLength, players[i].days[d].daily_times_str.length)
        maximumScoreLength = Math.max(maximumScoreLength, String(players[i].days[d].local_score).length)
    }
    for (let i = 0; i < players.length; i++) {
        let player = players[parseInt(htmlObjects[i].dataset.playerIndex)]
        htmlObjects[i].dataset.local_score_str = String(player.days[d].local_score).padStart(maximumScoreLength, " ")
        htmlObjects[i].dataset.local_score = player.days[d].local_score
        htmlObjects[i].dataset.first_star = player.days[d].first_star
        htmlObjects[i].dataset.second_star = player.days[d].second_star
        htmlObjects[i].dataset.second_star_offset = (player.days[d].second_star && player.days[d].first_star) ? player.days[d].second_star - player.days[d].first_star : undefined
        htmlObjects[i].children[lastSelectedDay + 1].textContent = "*"
        htmlObjects[i].children[d + 1].textContent = player.days[d].daily_times_str.padEnd(maximumTimesLength, " ")
    }
    lastSelectedDay = d
}

function sort(e) {
    toggleClass("activeSort", e.target)

    let attribute = e.target.dataset.attribute
    let inverted = e.target.dataset.inverted
    sortInternal(attribute, inverted)
    window.localStorage.setItem("sort", attribute)
}

function sortInternal(attribute, inverted) {
    let htmlObjects = [...document.getElementsByClassName("privboard-row")]
    let scoreboard = htmlObjects[0].parentElement
    htmlObjects.shift()

    htmlObjects.sort((a, b) => {
        if (a.dataset[attribute] === 'undefined') {
            return inverted
        }
        if (b.dataset[attribute] === 'undefined') {
            return inverted * -1
        }
        return (a.dataset[attribute] - b.dataset[attribute]) * inverted
    })

    let lastScore = 'undefined'
    let num = Math.ceil(Math.log10(players.length + 1))
    for (let i = 0; i < htmlObjects.length; i++) {
        scoreboard.appendChild(htmlObjects[i])
        if (lastScore === htmlObjects[i].dataset[attribute]) {
            htmlObjects[i].children[0].textContent = ''.padStart(num + 2, ' ')
        } else {
            htmlObjects[i].children[0].textContent = ` ${String(i+1).padStart(num, " ")})`
        }
        htmlObjects[i].childNodes[1].textContent = ` ${htmlObjects[i].dataset.local_score_str} `
        lastScore = htmlObjects[i].dataset[attribute]
    }
}

function createButton(text, attribute, inverted) {
    let element = document.createElement("a")
    element.href = "javascript:void(0)"
    element.dataset.attribute = attribute
    element.dataset.inverted = inverted
    element.textContent = `[${text}]`
    element.id = `sort-${attribute}`
    element.addEventListener("click", sort)
    return element
}

function setupSorting() {
    let scoreboard = document.getElementsByClassName("privboard-row")[0]
    let p = document.createElement("p")
    scoreboard.parentElement.insertBefore(p, scoreboard)
    p.appendChild(document.createTextNode("Sort by "))
    p.appendChild(createButton("Score", "local_score", -1))
    p.appendChild(document.createTextNode(", "))
    p.appendChild(createButton("First star", "first_star", 1))
    p.appendChild(document.createTextNode(", "))
    p.appendChild(createButton("Second star", "second_star", 1))
    p.appendChild(document.createTextNode(" or "))
    p.appendChild(createButton("Second star offset", "second_star_offset", 1))
    p.appendChild(document.createTextNode("."))


    let localSort = window.localStorage.getItem("sort")
    if (localSort !== null) {
        document.getElementById(`sort-${localSort}`).click()
    } else {
        document.getElementById(`sort-local_score`).click()
    }
}