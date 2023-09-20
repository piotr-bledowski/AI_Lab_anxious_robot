# AI_Lab_anxious_robot

## Jak uruchomić projekt
**Ze względu na dysktrybucję ROSa projekt najlepiej uruchomić na Ubuntu Jammy (22.04). Czy zadziała na Windowsie / innych systemach, tego nie wiem, nie zaszkodzi spróbować.**

### Co trzeba zainstalować:
- ROS Humble Hawksbill
- (być może) colcon, nie jestem pewien czy instaluje się automatycznie z ROSem, to jest narzędzie do kompilacji projektu
- Gazebo (Dokładnie Gazebo Classic, instalowane `sudo apt install gazebo`, to jest wprawdzie przestarzała i niewspierana dystrybucja, ale działa dużo lepiej niż nowsze)
- Python i CMake, ale one są raczej domyślnie zainstalowane na Ubuntu
- Resztę dependencies można sprawdzić w plikach package.xml w każdej paczce (tagi <exec_depend>)

### Uruchamianie wizualizacji i symulacji:
1. żeby móc używać komend ROSa w terminalu, należy użyć komendy `source /opt/ros/humble/setup.bash` (najlepiej dodać sobie to do .bashrc)
2. należy wykonywać poniższe komendy z poziomu folderu "anxious_robot_ws", czyli workspace projektu
3. kompilacja komendą `colcon build` (w innym miejscu niż anxious_robot_ws ta komenda stworzy nowe foldery "build", "install" i "log", stąd poprzedni punkt)
4. coś co zawsze robi się po kompilacji, `source install/setup.bash` to jest plik generowany przez colcon podczas kompilacji
5. `ros2 launch launch_config rviz_gazebo.launch.py` uruchomienie wizualizacji / symulacji jednym z plików launch, po nazwie można się domyślić który co uruchomi, taki najpełniejszy launch z komendy powyżej uruchamia RViz z osobnym oknem Joint State Publisher na manualne ruszanie stawami robota i równolegle Gazebo z pustym światem, w którym jest spawnowany robot (Na ten moment to co dzieje się w Gazebo nie jest synchronizowane z RViz, i.e. stan robota, w szczególności ruch kół)

### Manualne sterowanie robotem
Można publikować na topic /cmd_vel prosto z Terminala komendą ros2 topic pub, ale wygodniejszą opcją jest użycie ROSowego narzędzia do publikowania wiadomości Twist klawiaturą.
W celu sterowania robotem przy użyciu klawiatury należy otworzyć nowe okno terminala i uruchomić odpowiedni Node komendą `ros2 run teleop_twist_keyboard teleop_twist_keyboard`
