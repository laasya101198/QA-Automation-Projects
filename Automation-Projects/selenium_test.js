// Selenium WebDriver Test Automation with JavaScript & TestNG

const { Builder, By, Key, until } = require('selenium-webdriver');

(async function testGoogleSearch() {
    let driver = await new Builder().forBrowser('chrome').build();
    try {
        await driver.get('https://www.google.com');
        
        let searchBox = await driver.findElement(By.name('q'));
        await searchBox.sendKeys('Selenium WebDriver', Key.RETURN);
        
        await driver.wait(until.titleContains('Selenium WebDriver'), 5000);
        console.log('Test Passed: Google search executed successfully');
    } catch (error) {
        console.error('Test Failed:', error);
    } finally {
        await driver.quit();
    }
})();
