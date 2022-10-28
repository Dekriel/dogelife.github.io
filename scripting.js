var bal = 0

function init() {
    get("coin").innerHTML = bal;
}

function get(x)  {
    return document.getElementById(x);
}

function minigame() {
    location.href = 'rng';
}
