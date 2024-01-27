# Projekt Zespołu 10 - PWI

**Instrukcje**

Aby uruchomić projekt, należy:

1. Posiadać pythona oraz dowolny program, który go obsługuje (np. PyCharm)
2. Zainstalować bibliotekę pygame
3. Pobrać projekt z repozytorium githuba na swój komputer
4. Otworzyć projekt i uruchomić plik "main"


**Co udało, a czego nie udało nam się dodać**

1. SYSTEM GRY

Menu główne
Menu tworzenia sciezki
Ekran śmierci
Ekran wygranej
Gracz kupuje wieze i straznikow, aby powstrzymywać nadchodzące fale przeciwników.
Za zabijanie przeciwników dostaje złoto, a jeśli przeciwnik przeciwnik przejdzie całą ścieżkę to gracz traci HP

2. WROGOWIE

estetyczny wygląd dla każdego rodzaju wroga
wrogowie umierają
wrogowie mają różne statystyki (siła, szybkość zadawania obrażeń, odporność na atak wręcz, odporność na magię etc.)
9 fal wrogów
4 rodzaje wrogów
łatwy i intuicyjny system tworzenia nowych fal i nowych rodzajów wrogów (dla teoretycznego przyszłego rozwoju gry)
obrażenia dla gracza, kiedy wrogowi uda się pokonać ścieżkę
pieniądze za zabijanie wrogów

Czego nie udało się zaimplementować:

animacje ataku
animacje śmierci


3. WIEŻE

działają w obrębie własnego zasięgu
można postawić po wybraniu opcji ‘kup wieżę’ (naturalnie nie na samej 
ścieżce)
skupiają się na jednym wrogu, gdy ten pojawia się w ich zasięgu i znajdują 
nowego, gdy poprzedni znajdzie się poza zasięgiem
ranią wrogów co konkretny interwał

Czego nie udało się zaimplementować:

nowe (silniejsze) rodzaje wież przy kolejnych falach ataku

4. SOJUSZNICY
 
mają własny zasięg i podstawowe statystyki
po pojawieniu się na mapie idą na ścieżkę i czekają na wrogów
gdy wróg pojawi się w ich zasięgu, idą do niego po czym go atakują
giną gdy otrzymają wystarczająco obrażeń

Czego nie udało się zaimplementować:

różne rodzaje sojuszników
animacja śmierci


5.MAPA I ŚCIEŻKA

Można klikając w poszczególne punkty w edytorze ścieżki "narysować" trasę po której
będą chodzić wrogowie.

Czego nie udało się zaimplementować: 
Usuwanie ścieżki po ponownym rozpoczęciu (stare sprity 
ścieżki nie znikają).


#Credits
space.jpg by
https://www.freepik.com/free-photo/spaceship-orbits-dark-galaxy-glowing-blue-comet-generated-by-ai_40968215.htm#query=planet&position=23&from_view=keyword&track=sph&uuid=b92c4922-3efb-48fb-82c8-a7fe6f16d81f Image by vecstock on Freepik
