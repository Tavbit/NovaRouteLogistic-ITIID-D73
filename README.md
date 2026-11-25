# NovaRoute Logistics

Proyecto academico de IA para optimizacion de rutas de ultima milla.

## Equipo
- Emilio Iniestra: `backend/features/search`, `backend/features/optimization`
- Ricardo Diaz: `backend/features/machine_learning`, `backend/features/spark`, datasets y notebooks
- Gustavo Ovando: `frontend`, `backend/controllers`, `backend/services`, `backend/database`, integracion y CNN

## Arquitectura
- `frontend/`: interfaz Streamlit, paginas, componentes y servicios de presentacion.
- `backend/models/`: modelos de dominio.
- `backend/contracts/`: contrato comun aprobado por el equipo.
- `backend/controllers/`: adaptadores entre interfaz y servicios.
- `backend/services/`: coordinacion de casos de uso.
- `backend/features/`: algoritmos y modelos de IA.
- `backend/database/`: MongoDB y repositorios.
- `backend/data/`: grafo y datasets.
- `backend/tests/`: pruebas.

## Entorno inicial WSL2
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
python frontend/app.py
```

## Ramas
- `main`: estable
- `develop`: integracion
- `feature/search-algorithms`: Emilio
- `feature/machine-learning`: Ricardo
- `feature/app-integration`: Gustavo

No cambiar el contrato de datos ni las APIs comunes sin aprobacion del equipo.
