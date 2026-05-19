# Colombia Comparte User Journey Simulation

Final simulation project built with Python and Streamlit. The application models the Colombia Comparte entrepreneur registration flow using the exact states, base journeys, transition count matrix, transition probability matrix, simulation logic, and improvement proposal from `ProyectoFinalSimulacion.ipynb`.

## 🌐 Live Demo

👉 https://colombia-comparte-simulation.streamlit.app/?embed_options=light_theme

<img width="1918" height="871" alt="image" src="https://github.com/user-attachments/assets/57399a24-4e4f-485a-b2cb-407a9a904395" />

## Technology Choice

The interface uses **Streamlit** because it is the strongest fit for this project:

- It supports modern dashboards, sidebar navigation, tables, charts, and CSV export with little overhead.
- It is easier to deploy as a web app than Tkinter or PyQt6.
- It is more appropriate for analytics interfaces than Pygame.
- It keeps the project fully Python-based and simple to run locally.

## Project Files

- `app_simulacion_usuarios.py`: main Streamlit application.
- `ProyectoFinalSimulacion.ipynb`: original notebook used as the single source of truth for the model.
- `requirements.txt`: Python dependencies.
- `.gitignore`: local environment and cache exclusions.

## Model Data

The app uses the original notebook model:

- System: Colombia Comparte.
- Flow: entrepreneur registration.
- States: `S0` to `S29`.
- Initial state: `S0`.
- Successful final state: `S28`.
- Abandonment states: `S20`, `S21`, `S22`, `S23`.
- Error states: `S24`, `S29`.
- Base journeys: 60 user journeys.
- Improvement scenario: lower risk around `S24` and reduce document-upload abandonment associated with `S16`.

## Requirements Covered

- Select the number of users to simulate.
- Select the maximum number of steps per user.
- Display model states with code, name, description, and state type.
- Display the base user journeys.
- Display the transition count matrix.
- Display the transition probability matrix.
- Run the user simulation from the interface.
- Display a preview of simulated users.
- Display success, abandonment, error, support/follow-up usage, and average steps.
- Include modern result charts.
- Identify the critical state among non-successful outcomes.
- Provide a recommendation and improvement interface linked to the critical state.

## Installation

Python 3.11 or 3.12 is recommended. Python 3.14 may work with the latest dependencies, but some scientific packages can lag behind newer Python releases.

Open PowerShell in the project folder:

```powershell
cd "C:\Users\leonc\OneDrive\Documentos\New project"
```

Create a virtual environment:

```powershell
py -3.12 -m venv .venv
```

If Python 3.12 is not installed, use your available Python launcher:

```powershell
py -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

If pip shows `uninstall-no-record-file`, repair it first:

```powershell
python -m pip install --ignore-installed --no-deps pip==25.3
python -m pip install -r requirements.txt
```

## Running the App

With the virtual environment active, run:

```powershell
streamlit run app_simulacion_usuarios.py
```

Open the local URL if it does not launch automatically:

```text
http://localhost:8501
```

## How to Use

1. Select the number of users in the sidebar.
2. Select the maximum number of steps per user.
3. Adjust the random seed if you want reproducible or varied results.
4. Click **Ejecutar simulación**.
5. Use the sidebar navigation:
   - **Dashboard**: KPIs and charts.
   - **Modelo**: states, base journeys, count matrix, and probability matrix.
   - **Simulación**: simulated user preview and full result table.
   - **Mejora**: critical state, recommendation, and improved scenario comparison.

