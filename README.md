# FishJoy
This website was created to help fishermen from all over the world to get important information about particular
spot, fish on this spot and of course the best baits for fish that you want to catch. For convinient usage, website provides
weather forecast for particular location and also a marker on map.

You can divide fish and spots on particular categories, like peaceful or predatory, river or lake respectively etc.

If you have something to share or offer, you can easily do that by filling the form. If you do a mistake when added spot/fish/bait and
want to change it, just press the button edit/delete on the page of full information about spot/fish/bait.
You can modify or delete only spots/fish/baits that you own.

Telegram bot extension : https://github.com/Rotmanss/FishJoy_Bot

For extra questions you can text on romanromapev@gmail.com.

Important: you have to be authorized to fill the form!

## Running with Docker

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rotmanss/FishJoy.git
   cd FishJoy/FishJoy
   ```

2. **Start the application:**
   ```bash
   docker compose up
   ```
   The first run will take a few minutes to download images and install dependencies.

3. **Access the application:**
   - Open your browser: **http://localhost:8000**

4. **Create an admin user:**
   
   Open a new terminal and run:
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```
   Then access the admin panel at: **http://localhost:8000/admin**

5. **Stop the application:**
   
   Press `Ctrl+C` in the terminal, then run:
   ```bash
   docker compose down
   ```

### What's Running?
- **PostgreSQL 15** database (port 5432, internal)
- **Django** web application (port 8000)
- Database data persists in Docker volumes

### Useful Commands
```bash
# Start in background (detached mode)
docker compose up -d

# View logs
docker compose logs -f

# Stop and remove all containers
docker compose down

# Stop and remove all data (fresh start)
docker compose down -v
```
