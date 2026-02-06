const map = L.map("map").setView([10.76, 106.66], 10);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);
const tourId = window.location.pathname.split('/')[3];
fetch("/tours/map_stops/" + tourId)
  .then((response) => response.json())
  .then((tours) => {
    const bounds = [];

    tours.forEach((tour) => {
      const marker = L.marker([tour.lat, tour.lng]).addTo(map).bindPopup(`
          <b>${tour.name}</b><br>
          <a href="/tours/detail/${tour.id}">Xem chi tiết</a>
        `);

      bounds.push([tour.lat, tour.lng]);
    });

    if (bounds.length > 0) {
      map.fitBounds(bounds);
    }
  });
