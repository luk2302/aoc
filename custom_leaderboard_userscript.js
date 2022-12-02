// ==UserScript==
// @name         AOC custom score board
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  AOC custom score board
// @author       Lukas Rinke
// @match        https://adventofcode.com/2022/leaderboard/private/view/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=adventofcode.com
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    fetch(`${document.location.href.split("/").at(-1)}.json`).then(function(response) {
        return response.json();
    }).then(function(data) {
        handle(data);
    });
})();

function handle(DATA) {
    let members = Object.keys(DATA.members).map(function (key) {
        return DATA.members[key];
    });

    members = members.filter(member => member.local_score !== 0)
    members.sort((a, b) => b.local_score - a.local_score)

    let now = new Date()
    let day_to_check = now.getUTCHours() < 6 ? now.getUTCDate() - 1 : now.getUTCDate()
    let start_of_aoc_day_ts = new Date(Date.UTC(2022, 11, day_to_check, 5)).getTime() / 1000

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

    var maximum_score_length = 0
    members = members.map(function (member) {
        let first_star = member.completion_day_level[day_to_check.toString()]?.["1"]?.get_star_ts
        let second_star = member.completion_day_level[day_to_check.toString()]?.["2"]?.get_star_ts
        let daily_score_str = `* (${showTime(start_of_aoc_day_ts, first_star)} / ${showTime(start_of_aoc_day_ts, second_star)})`
        maximum_score_length = Math.max(maximum_score_length, daily_score_str.length)
        return {
            "name": member.name,
            "local_score": member.local_score,
            "daily_score_str": daily_score_str,
            "first_star": first_star,
            "second_star": second_star
        }
    })

    let html_objects = [...document.getElementsByClassName("privboard-row")]
    html_objects.shift()

    for (let i = members.length; i < html_objects.length; i++) {
        html_objects[i].remove()
    }
    for (let i = 0; i < members.length; i++) {
        html_objects[i].dataset.local_score = members[i].local_score
        html_objects[i].dataset.first_star = members[i].first_star
        html_objects[i].dataset.second_star = members[i].second_star
        html_objects[i].children[day_to_check].textContent = members[i].daily_score_str.padEnd(maximum_score_length, " ")
    }

    setupSorting()
}

function sort(e) {
    let attribute = e.target.dataset.attribute
    let inverted = e.target.dataset.inverted
    let html_objects = [...document.getElementsByClassName("privboard-row")]
    let scoreboard = html_objects[0].parentElement
    html_objects.shift()

    html_objects.sort((a, b) => (a.dataset[attribute] - b.dataset[attribute])* inverted)

    for (let i = 0; i < html_objects.length; i++) {
        scoreboard.appendChild(html_objects[i])
        html_objects[i].children[0].textContent = ` ${String(i+1).padStart(2, " ")})`
    }
}

function addButton(text, attribute, inverted) {
    let element = document.createElement("a")
    element.href = "javascript:void(0)"
    element.dataset.attribute = attribute
    element.dataset.inverted = inverted
    element.textContent = `[${text}]`
    element.addEventListener("click", sort)
    return element
}

function setupSorting() {
    let scoreboard = document.getElementsByClassName("privboard-row")[0]
    let p = document.createElement("p")
    scoreboard.parentElement.insertBefore(p, scoreboard)
    p.appendChild(document.createTextNode("Sort by "))
    p.appendChild(addButton("Score", "local_score", -1))
    p.appendChild(document.createTextNode(", "))
    p.appendChild(addButton("First star", "first_star", 1))
    p.appendChild(document.createTextNode(" or "))
    p.appendChild(addButton("Second star", "second_star", 1))
    p.appendChild(document.createTextNode("."))
}