# AI_Lab_anxious_robot

## Jak uruchomić projekt
**Ze względu na dysktrybucję ROSa projekt zadziała wyłącznie na Ubuntu Jammy.**

### Co trzeba zainstalować (najlepiej posłużyć się dokumentacjami):
- ROS Humble Hawksbill
- (być może) colcon, nie jestem pewien czy instaluje się autoamtycznie z ROSem, to jest narzędzie do kompilacji projektu
- Gazebo Fortress
- Python i CMake, ale one są raczej domyślnie zainstalowane na Ubuntu

### Uruchamianie wizualizacji i symulacji:
1. żeby móc używać komend ROSa w terminalu, należy użyć komendy `source /opt/ros/humble/setup.bash` (najlepiej dodać sobie to do .bashrc)
2. należy wykonywać poniższe komendy z poziomu folderu "anxious_robot_ws", czyli workspace projektu
3. kompilacja komendą `colcon build` (w innym miejscu niż anxious_robot_ws ta komenda stworzy nowe foldery "build", "install" i "log", stąd poprzedni punkt)
4. coś co zawsze robi się po kompilacji, `source install/setup.bash` to jest plik generowany przez colcon podczas kompilacji
5. `ros2 launch launch_config rviz_gazebo.launch.py` uruchomienie wizualizacji / symulacji jednym z plików launch, po nazwie można się domyślić który co uruchomi, taki najpełniejszy launch z komendy powyżej uruchamia RViz z osobnym oknem Joint State Publisher na manualne ruszanie stawami robota i równolegle Gazebo z pustym światem, w którym jest spawnowany robot (Na ten moment to co dzieje się w Gazebo nie jest synchronizowane z RViz, i.e. stan robota, w szczególności ruch kół)
