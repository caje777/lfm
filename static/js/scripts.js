document.addEventListener('DOMContentLoaded', function() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('data-container');
            data.recenttracks.track.forEach(track => {
                const trackElement = document.createElement('div');
                trackElement.textContent = `${track.artist['#text']} - ${track.name}`;
                container.appendChild(trackElement);
            });
        });
});
