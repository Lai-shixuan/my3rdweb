document.getElementById('select-folder').addEventListener('click', () => {
    window.electronAPI.selectFolder();
});

window.electronAPI.onFolderSelected((event, imagePath) => {
    const img = new Image();
    img.src = imagePath;
    img.onload = () => {
        document.getElementById('original-image').src = imagePath;

        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.rotate(90 * Math.PI / 180);
        ctx.drawImage(img, 0, -img.height);

        const rotatedImageSrc = canvas.toDataURL();
        document.getElementById('rotated-image').src = rotatedImageSrc;
        document.getElementById('download-button').onclick = () => {
            const link = document.createElement('a');
            link.href = rotatedImageSrc;
            link.download = 'rotated-image.png';
            link.click();
        };
        document.getElementById('download-button').style.display = 'block';
    };
});
