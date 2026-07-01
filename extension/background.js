// Open the side panel when the extension is installed
chrome.runtime.onInstalled.addListener(() => {
    
    // Enable opening the side panel by clicking the extension icon
    chrome.sidePanel.setPanelBehavior({
        openPanelOnActionClick: true
    });
});
