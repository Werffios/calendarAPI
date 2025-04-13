# 📅 Servicio de Verificación de Festivos en Colombia

**API REST** desarrollada con **FastAPI** que permite verificar si una fecha específica es un día festivo en **Colombia**.

---

## ✨ Características

- ✅ Verificación de días festivos en Colombia  
- ⚡ Endpoint simple y fácil de usar  
- 🐳 Dockerizado para facilitar su despliegue  
- 📘 Documentación automática con Swagger UI y ReDoc  

---

## 🧰 Requisitos previos

- Python 3.12 o superior  
- Docker y Docker Compose *(opcional, para despliegue containerizado)*  

---

## 🚀 Instalación

### 🔧 Opción 1: Ejecución local

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Werffios/calendarAPI.git
   cd calendarAPI
   ```

2. Crea un entorno virtual e instala las dependencias:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Inicia el servidor local:

   ```bash
   uvicorn main:app --reload
   ```

---

### 🐋 Opción 2: Ejecución con Docker

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Werffios/calendarAPI.git
   cd calendarAPI
   ```

2. Crea la red Docker si no existe:

   ```bash
   docker network create --subnet=192.168.10.0/24 net
   ```

3. Levanta los servicios:

   ```bash
   docker-compose up -d
   ```

---

## 📡 Uso de la API

### 1. **Ruta principal**

`GET /`

**Respuesta:**

```json
{
  "message": "Hello World"
}
```

---

### 2. **Verificación de festivos**

`GET /festivo/{fecha}`

- Formato de `{fecha}`: `yyyy-mm-dd`  
- Ejemplo: `/festivo/2023-01-01`

**Respuesta esperada:**

```json
{
  "fecha": "2023-01-01",
  "festivo": true,
  "nombre_festivo": "Año Nuevo"
}
```

---

## 📖 Documentación de la API

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)  
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🌐 Acceso a la aplicación

- 📍 *Ejecutando con Docker*:  
  http://192.168.10.31:5000  

- 🖥️ *Ejecutando localmente*:  
  http://localhost:8000  
