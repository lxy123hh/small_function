document.addEventListener('DOMContentLoaded', function () {
    const totalImages = 100; // 图片总数
    let previousIndex = -1; // 记录上次随机索引

    function getRandomIndex(previousIndex) {
        let randomIndex;
        do {
            randomIndex = Math.floor(Math.random() * totalImages) + 1;
        } while (randomIndex === previousIndex);
        return randomIndex;
    }

    function changeBackground_img() {
        const randomIndex = getRandomIndex(previousIndex);
        const img = new Image();
        img.src = `/static/notes_picture/background/${randomIndex}.jpg`;


        // 确保图片加载完成后再设置为 body 的背景图
        img.onload = function () {
            document.body.style.backgroundImage = `url(${img.src})`;
            document.body.style.backgroundSize = 'cover'; // 确保背景图覆盖整个页面
            document.body.style.backgroundPosition = 'center'; // 背景图居中
            document.body.style.backgroundAttachment = 'fixed'; // 背景图固定
            previousIndex = randomIndex; // 更新前一个索引
        }
    }

    changeBackground_img();
    setInterval(changeBackground_img, 10000); // 每10秒换一次背景图
});
