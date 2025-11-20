# 🌐 Weather API Project – User Stories

## 1. Use Case Diagram (Top Level)

**Actors:**
- **User** – enters the city name, views the result  
- **Weather API** – provides weather data  

**Main Functions (Use Cases):**
1. Enter city name  
2. Request weather data from API  
3. Display current weather  
4. Handle errors (e.g., wrong city input)  
5. Optional: show forecast for several days  

---

## 2. User Stories (Middle Level)

### Function 1: Enter city name
- **User Story 1.1**  
  - As a user  
  - I want to type in the name of a city  
  - So that I can get weather information for it  
  - **Story Points:** 2  

**Tasks:**  
- [ ] Create input field for city name  
- [ ] Add button to confirm request  

---

### Function 2: Request weather data from API
- **User Story 2.1**  
  - As a system  
  - I want to send a request with city name and API key  
  - So that I can retrieve current weather data in JSON  
  - **Story Points:** 3  

**Tasks:**  
- [ ] Implement API request function  
- [ ] Store API key securely  
- [ ] Parse JSON response  

---

### Function 3: Display current weather
- **User Story 3.1**  
  - As a user  
  - I want to see the temperature, humidity, and condition of the city  
  - So that I understand the weather right away  
  - **Story Points:** 5  

- **User Story 3.2 (branch)**  
  - As a user  
  - I want weather icons or emojis (☀️ 🌧️ ❄️)  
  - So that the information is more visual and easier to read  
  - **Story Points:** 3  

**Tasks:**  
- [ ] Display temperature, humidity, and condition in UI  
- [ ] Add support for weather icons/emojis  

---

### Function 4: Handle errors
- **User Story 4.1**  
  - As a user  
  - I want to see a clear error message if I type a wrong city name  
  - So that I can correct it quickly  
  - **Story Points:** 2  

- **User Story 4.2**  
  - As a system  
  - I want to handle API errors (e.g., invalid key, no response)  
  - So that I don’t crash and can inform the user  
  - **Story Points:** 3  

**Tasks:**  
- [ ] Validate user input (city name)  
- [ ] Show error message in UI  
- [ ] Catch API request errors and display message  

---

### Function 5 (Optional): Show forecast for several days
- **User Story 5.1**  
  - As a user  
  - I want to see a 3-day or 5-day weather forecast  
  - So that I can plan my activities  
  - **Story Points:** 8  

**Tasks:**  
- [ ] Extend API request for forecast endpoint  
- [ ] Parse and display multiple days of weather  
- [ ] Add navigation (e.g., tabs or cards)  

---

## 3. Obstacles (Examples)
- 🖨️ No paper in the printer → easy to fix (low impact)  
- 🖥️ Server too slow → need more memory or optimization  
- 👥 Team members conflict → Scrum Master resolves the issue  

---

## 4. Meetings (Scrum Rituals)
- **Sprint Planning:** move user stories from Product Backlog → Sprint Backlog  
- **Daily Stand-up:** 15 min daily (what was done / what is next / obstacles)  
- **Sprint Grooming (optional):** split big items into smaller tasks  
- **Sprint Review:** present working functionality  
- **Sprint Retrospective:** discuss improvements as a team  

---

## 5. Sprint Info
- Total: **2 sprints**, each lasting 2 weeks  
- After 4 weeks: project demonstration with working functionality  
- Mandatory artifacts:  
  - GitHub repository  
  - Markdown documentation (`README.md`, `UserStories.md`)  
  - Trello board  
  - GitHub Pages (presentation/documentation)  
  - WOW effect ✨  


