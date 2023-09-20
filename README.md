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


## Struktura projektu (co gdzie ma swoje miejsce)
Pracujemy wyłącznie w folderze src, tam idzie cały kod źródłowy, reszta zawartości workspace to pliki generowane przez colcon podczas kompilacji.
Projekt dzieli się na paczki w imię przejrzystości. Każda paczka (ROS package) odpowiada za jedną część projektu. Na ten moment paczki są 3, będzie ich więcej kiedy zaczniemy pracę nad autonomicznym poruszaniem się robota i lękiem warunkowym.

### bringup
Ta paczka zawiera kod potrzebny do uruchomienia projektu, podzielony na 2 części. Tą ważniejszą jest launch - tam trzymamy wszystkie pliki launch, które prawdopodobnie często będą modyfikowane wraz z rozwojem projektu.
Drugą częścią tej paczki jest config, tam jest domyślna konfiguracja RViz (tego właściwie można nie czytać i nie ruszać), której potrzebujemy do uruchomienia programu z pliku launch. Ale jeśli są jakieś inne konfiguracyjne pliki YAML potrzebne przy launchowaniu projektu, to tam jest ich miejsce.

### robot_description
W tej paczce do folderu urdf idą jak nazwa wskazuje pliki URDF, czyli opis naszego robota publikowany do RViz i Gazebo. Ilość kodu rośnie tutaj dość szybko wraz z kolejnymi elementami (szczególnie część związana z Gazebo), w związku z czym rozbiłem to na kilka plików. Ogólnie ten XMLowy kod powinien być dość samo-wyjaśnialny.

### simulation
Tutaj do folderu worlds idą różne konfiguracje Gazebo. Chyba nie ma potrzeby nic ręcznie tam pisać. Jeśli ktoś robi nowy świat w Gazebo, jakiś labirynt / przeszkody dla naszego robota, najlepiej poustawiać wszystko w samym Gazebo (bez robota na scenie żeby się nie duplikował przy uruchamianiu projektu) po czym zapisać świat do pliku SDF `File -> Save World As` i zapisać właśnie w tym dedykowanym do tego miejscu w projekcie.

**Dobre praktyki**:
- Jeśli w paczce jest używany kod z innych paczek, tych z projektu lub tych z ROS, dobrze jest dodać je jako dependency w tagu <exec_depend> w pliku package.xml danej paczki. Żeby było wiadomo czego dana paczka potrzebuje do działania.
- W tym samym pliku package.xml jest miejsce na opisanie paczki, wymienienie autorów itp. w odpowiednich tagach, warto to robić.
- Jeśli paczka nie zawiera żadnych pisanych przez nas ROS Node'ów, lepiej żeby to była paczka C++, wtedy można usunąć foldery src oraz include i wtedy z konfiguracyjnych rzeczy zostaje tylko CMakeLists.txt i package.xml, więc jest dość czysto.

