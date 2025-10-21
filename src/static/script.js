async function fetchWeather(lang = "en") {
  const mainDiv = document.getElementById("mainWeather");
  const forecastDiv = document.getElementById("forecast");
  const animContainer = document.getElementById("animationContainer");
  const forecastTitle = document.getElementById("forecastTitle");

  mainDiv.innerHTML = `<div class="loader">${getText("loading", lang)}</div>`;
  forecastDiv.innerHTML = "";

  try {
    const res = await fetch("/weather", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ lang }),
    });
    const data = await res.json();

    if (res.ok) {
      // Обновляем всё, включая город
      mainDiv.innerHTML = `
        <h1 class="city-name">${data.city}, ${data.country}</h1>
        <div class="temp">${data.temp}°C</div>
        <div class="condition">${data.condition}</div>
        <div class="details">
          ${getText("humidity", lang)}: ${data.humidity}%<br>
          ${getText("wind", lang)}: ${data.wind_speed} km/h (${data.wind_dir})<br>
          ${getText("pressure", lang)}: ${data.pressure} mbar<br>
          ${getText("feels_like", lang)}: ${data.feels_like}°C
        </div>
      `;

      forecastTitle.textContent = getText("forecast_title", lang);

      // теперь не обрезаем прогноз — показываем все дни, которые вернул API
      forecastDiv.innerHTML = data.forecast
        .map(
          (day) => `
          <div class="forecast-day">
            <p>${day.date}</p>
            <p>${day.condition}</p>
            <p>${getText("temp", lang)}: ${day.avg_temp}°C</p>
            <p>${getText("rain", lang)}: ${day.rain}%</p>
          </div>`
        )
        .join("");

      createWeatherAnimation(data.condition, animContainer);
    } else {
      mainDiv.innerHTML = `<p>${data.error || "Error loading weather"}</p>`;
    }
  } catch (e) {
    mainDiv.innerHTML = `<p>Error: ${e.message}</p>`;
  }
}

function createWeatherAnimation(condition, container) {
  container.innerHTML = "";
  condition = condition.toLowerCase();

  if (condition.includes("rain")) {
    for (let i = 0; i < 80; i++) {
      const drop = document.createElement("div");
      drop.className = "rain-drop";
      drop.style.left = Math.random() * 100 + "%";
      drop.style.animationDelay = Math.random() + "s";
      drop.style.height = 8 + Math.random() * 10 + "px";
      container.appendChild(drop);
    }
  } else if (condition.includes("sun") || condition.includes("clear")) {
    const sun = document.createElement("div");
    sun.className = "sun";
    container.appendChild(sun);
  }
}

function getText(key, lang) {
  const dict = {
    loading: { en: "Loading weather...", ru: "Загрузка погоды...", hu: "Időjárás betöltése..." },
    humidity: { en: "Humidity", ru: "Влажность", hu: "Páratartalom" },
    wind: { en: "Wind", ru: "Ветер", hu: "Szél" },
    pressure: { en: "Pressure", ru: "Давление", hu: "Nyomás" },
    feels_like: { en: "Feels like", ru: "Ощущается как", hu: "Hőérzet" },
    forecast_title: { en: "5-day forecast", ru: "Прогноз на 5 дней", hu: "5 napos előrejelzés" },
    temp: { en: "Temperature", ru: "Температура", hu: "Hőmérséklet" },
    rain: { en: "Chance of rain", ru: "Вероятность дождя", hu: "Eső valószínűsége" },
  };
  return dict[key]?.[lang] || dict[key]?.en || key;
}

document.getElementById("langSelect").addEventListener("change", (e) => {
  const lang = e.target.value;
  fetchWeather(lang);
});

window.addEventListener("load", () => fetchWeather("en"));


