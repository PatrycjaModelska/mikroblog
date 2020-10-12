#Serwis do mikroblogowania
    Celem projektu było utworzenie serwisu do mikroblogowania.
    Aplikacja utrwala materiał z zakresu Django.

### O projekcie
    Dostępne funkcjonalności:
    1. Rejestracja/logowanie/wylogowanie.
    2. Wyszukiwanie postów (po treści/tytule, po autorze, według kategorii).
    3. Dodawanie komentarzy.
    4. Dodwanie postów.
    5. Zarządzanie postami (edycja, usuwanie).
    6. Ocenianie postów (przyznawanie punktów w skali od 1 do 5).

    Funckjonalności 4-6 dostępne są jedynie dla zalogowanych użytkowników. 

### Uruchomienie projektu 
    1. Wymagania sprzętowe:
    
            python 3.6
            
    2. Tworzenie środowiska w konsoli:
    
            python -m venv myvenv
            cd myvenv/Scripts/activate
            
    3. Ściąganie repozytorium:
    
            git clone https://github.com/PatrycjaModelska/Microblog.git
    
    4. Instalowanie wymaganych plików:
    
            pip install -r requirements.txt.
    
    5. Utworzenie super użytkownika:
    
            python manage.py createsuperuser
    
    6. Migracja danych do tabel w bazie:
    
            python manage.py makemigrations
            python manage.py migrate
            
    7. Uruchomienie serwera:
    
            python mamage.py runserver
            
            
### Wersja demo
    Możesz pominąć krok ze ściąganiem repozytorium i przejść do wersji demo:
    https://mikroblog-demo.herokuapp.com/

### Autorzy
    Patrycja, Żaneta, Dawid