// 获取要更新的元素
var timeElement = document.getElementById('current-time');

// 更新时间的函数
function updateTime() {
    // 使用 moment.js 获取当前时间，并格式化为指定的格式
    var currentTime = moment().format('YYYY-MM-DD HH:mm:ss');

    // 更新元素的文本内容为当前日期时间
    timeElement.textContent = '当前时间: ' + currentTime;
}

// 定时器，每秒更新一次时间
setInterval(updateTime, 10);
