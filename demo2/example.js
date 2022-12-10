const map = L.map('map').setView([60.23, 24.74], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

const airportMarkers = L.featureGroup().addTo(map);
let attempt_left = 5;
let totalScore = 0;
// Choose from list *****************************
const continentList = document.querySelector('#continents');
const countryList = document.querySelector('#countries');
const airportList = document.querySelector('#airports');

// Start with adding continents
async function showContinents() {
  const response = await fetch('http://127.0.0.1:3000/continents');
  const continents = await response.json();
  for (const cont of continents) {
    const option = document.createElement('option');
    option.value = cont.continent;
    option.innerText = cont.continent;
    continentList.appendChild(option);
  }
}

showContinents(); // this starts the loading of continents

// when continent is selected get countries and add to second list...
continentList.addEventListener('change', async function() {
  countryList.innerHTML = '<option>Select Country</option>'; // empty the country and airport lists because the user might change continent
  airportList.innerHTML = '<option>Select Airport</option>';
  const response = await fetch(
      'http://127.0.0.1:3000/countries/' + continentList.value);
  const countries = await response.json();
  for (const country of countries) {
    const option = document.createElement('option');
    option.value = country.iso_country;
    option.innerText = country.name;
    countryList.appendChild(option);
  }
});

// when country is selected get airports and add to third list...
countryList.addEventListener('change', async function() {
  airportList.innerHTML = '<option>Select Airport</option>'; // empty the airport list because the user might change country
  const response = await fetch(
      'http://127.0.0.1:3000/airports/' + countryList.value);
  const airports = await response.json();
  for (const airport of airports) {
    const option = document.createElement('option');
    option.value = airport.ident;
    option.innerText = airport.name;
    airportList.appendChild(option);
  }
});

// when airport is selected show it on the map...
airportList.addEventListener('change', async function() {

  const response = await fetch(
      'http://127.0.0.1:3000/airport/' + airportList.value);
  const airport = await response.json();
  console.log(airport);
  // remove possible other markers
  airportMarkers.clearLayers();
  // add marker
  const marker = L.marker([airport.latitude_deg, airport.longitude_deg]).
      addTo(map).
      bindPopup(airport.name).
      openPopup();
  airportMarkers.addLayer(marker);
  // pan map to selected airport
  map.flyTo([airport.latitude_deg, airport.longitude_deg]);
  console.log(airport.name);
  const score = await fetch('http://127.0.0.1:3000/weather/' + airport.name);
  const result = await score.json();
  console.log(result);
  const newArray = result;
  console.log(newArray);
  console.log(newArray.temp);
  const temperature = document.querySelector("#temperature");
  Kel_deg = newArray.temp - 273.15
  temperature.innerHTML =  Kel_deg.toFixed(2);
  const humidity = document.querySelector("#humidity");
  humidity.innerHTML = newArray.humidity;
  const feelsLike = document.querySelector("#feels-like");
  fel_deg = newArray.feels_like - 273.15
  feelsLike.innerHTML = fel_deg.toFixed(2);

  attempt_left--;
  if(attempt_left == 0){
    alert("Game Over!")
  }else {
    const attempt = document.querySelector("#Attempt_left");
    attempt.innerHTML = attempt_left.toString();
    const airportName = document.querySelector("#airport-name");
    //airportName.innerHTML = ""
    if (Math.random() <= 0.5) {
      totalScore += 500;
      airportName.innerHTML = "Treasure Status: Congrats! you have found the treasure";
    } else {
      totalScore += 0;
      airportName.innerText= "Treasure Status: Oops! No Treasure. Better luck in next destination";
    }

    const scoreBoard = document.querySelector("#total_score");
    scoreBoard.innerHTML = totalScore;
    const airportnamee = document.querySelector("#airport-namee");
    airportnamee.innerHTML = "Current location: " + airport.name;


  }
});

// *********************************************