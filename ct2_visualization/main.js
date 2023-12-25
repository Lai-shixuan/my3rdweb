const { app, BrowserWindow, ipcMain, dialog } = require('electron');
const fs = require('fs');
const path = require('path');

function createWindow() {
    const mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js')
        }
    });

    mainWindow.loadFile('index.html');
}

app.whenReady().then(createWindow);

ipcMain.on('select-folder', async (event) => {
    const window = BrowserWindow.getFocusedWindow();
    const result = await dialog.showOpenDialog(window, {
        properties: ['openDirectory']
    });

    if (!result.canceled && result.filePaths.length > 0) {
        const folderPath = result.filePaths[0];
        fs.readdir(folderPath, (err, files) => {
            if (err) {
                console.error('Error reading directory', err);
                return;
            }

            const imageFile = files.find(file => /\.(jpg|jpeg|png|bmp|gif)$/i.test(file));
            if (imageFile) {
                event.reply('folder-selected', path.join(folderPath, imageFile));
            }
        });
    }
});
