#/bin/bash
case "$1" in
    "run_dev")
        echo "Running development server and client"
        export ON_PI=false
        gnome-terminal -e 'python dev_main.py'
        gnome-terminal -e 'npm start --prefix client'
        ;;
    "run_live_without_pimote")
        echo "Running live server and client without the Pi-Mote"
        export ON_PI=false
        gunicorn --bind 0.0.0.0:5678  live_main:app --workers 1
        ;;
    "run_live_with_pimote")
        echo "Running live server and client with the Pi-Mote"
        export ON_PI=true
        gunicorn --bind 0.0.0.0:5678  live_main:app --workers 1
        ;;
    "build_client")
        echo "Building Light Controller Client"
        npm run build --prefix client
        ;;
    *)
        echo "Unrecognised argument '$1'."
        exit 1
        ;;
esac