Poniżej zamieszczone dane zawierają zapisy EEG z trzykrotnej kalibracji interfejsu mózg-komputer opartej o potencjał P300
wykonanej zgodnie z opisem przedstawionym na Laboratorium EEG [1]: Plik:Dane kalibracja p300.tar.gz

Zawartość archiwum to:

	Trzy zestawy danych zawierające macierze X (przykłady x cechy), Y - opisująca kategorię przykładów (1- target, 0 - non-target).
	p300_DS1.mat
	p300_DS2.mat
	p300_DS3.mat

	Funkcja przygotowująca zestawy danych
	csp.m

	Surowe dane:
	test1__calibration_p300.obci.raw
	test1__calibration_p300.obci.tag
	test1__calibration_p300.obci.xml
	test2__calibration_p300.obci.raw
	test2__calibration_p300.obci.tag
	test2__calibration_p300.obci.xml
	test3__calibration_p300.obci.raw
	test3__calibration_p300.obci.tag
	test3__calibration_p300.obci.xml

Sygnały zostały "zmontowane" za pomocą filtra przestrzennego CSP [2]. Cechami wyliczonymi dla każdego przykładu są wariancje uśrednionych 
po 8 realizacjach sygnałów w odcinku 150 do 550 ms po bodźcu dla kadego ze źródeł estymowanych przez CSP [3]. 
Zadaniem projektowym jest zaprojektowanie klasyfikatora, który wyuczony na danych ze zbioru p300_DS1.mat miałby możliwie najlepszą 
klasyfikację na dwóch pozostałych zbiorach i przedstawienie wyników porównawczych dla różnych klasyfikatorów z wykorzystaniem technik 
opisanych tu: https://brain.fuw.edu.pl/edu/index.php/Uczenie_maszynowe_i_sztuczne_sieci_neuronowe/Wyk%C5%82ad_Ocena_jako%C5%9Bci_klasyfikacji.

[1]https://brain.fuw.edu.pl/edu/index.php/Laboratorium_EEG/CSP#Eksperyment
[2]https://brain.fuw.edu.pl/edu/index.php/Laboratorium_EEG/CSP#Common_Spatial_Pattern
[3]https://brain.fuw.edu.pl/edu/index.php/Laboratorium_EEG/CSP#.C5.9Alepa_separacja_.C5.BAr.C3.B3de.C5.82
