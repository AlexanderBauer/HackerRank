let t = '', res = _ => document.getElementById('res').innerHTML = t = _;
document.getElementById('btns').addEventListener('click', e => {
    if (e.target.id === 'btnClr') res(''); else
    if (e.target.id === 'btnEql') res((eval(t.replace(/[01]+/g, '0b$&')) >> 0).toString(2)); else
    res(t + e.target.innerHTML);
})