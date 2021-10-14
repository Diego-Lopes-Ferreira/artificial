const { app, BrowserWindow } = require("electron");
// The app module, which controls your application's event lifecycle.
// The BrowserWindow module, which creates and manages application windows.

const win_config = {
  width: 800,
  height: 600,
};

function create_window() {
  const win = new BrowserWindow(win_config);
  win.loadFile("ui/index.html");
}

app.whenReady().then(() => {
  create_window();
  app.on("activate", function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on("window-all-closed", function () {
  if (process.platform !== "darwin") app.quit();
});
