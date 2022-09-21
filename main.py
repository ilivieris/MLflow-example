# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Libraries
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
import uvicorn


if __name__ == "__main__":
    # uvicorn.run("app.app:app") # Runs on 127.0.0.1:8000 by default

    uvicorn.run('application.app:app', 
                host          = "0.0.0.0", 
                port          = 8000, 
                log_level     = "info",
                proxy_headers = True, 
                reload        = True)