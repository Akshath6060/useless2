const getFortuneBtn = document.getElementById('getFortuneBtn');
const fortuneText = document.getElementById('fortuneText');

getFortuneBtn.addEventListener('click', async () => {
    try {
        const response = await fetch('http://localhost:8000/generate-fortune');
        const data = await response.json();
        fortuneText.textContent = data.response;
    } catch (error) {
        console.error('Error fetching fortune:', error);
        fortuneText.textContent = 'Error fetching fortune. Please try again later.';
    }
});