document.addEventListener('DOMContentLoaded', () => {
    const tickerInput = document.getElementById('tickerInput');
    const tickerButton = document.getElementById('tickerId')

    console.log("javascript works");


    tickerButton.addEventListener('click', (e) => {
        e.preventDefault();
        const tickerInputContent = tickerInput.value;
        tickerInput.click();
        console.log(tickerInputContent)
    });
    })