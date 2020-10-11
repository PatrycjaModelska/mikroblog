#Serwis do mikroblogowania
    Celem projektu jest utworzenie srrwisu do zakładania oraz przeglądania mikroblogów.
    Jest to aplikacja utrwalająca materiał z zakresu django.

### O projekcie
    Microblog jest serwisem do tworzenia mikroblogów. 
    Dostępne moduły:
    1. Rejestracja:
        Przy rejestracji użytkownik podaje imię, nazwisko, username, email, hasło oraz avatar
        Pola obiwiązkowe to username, eamil oraz hasło.Pozostałe pola opcjonalne
    2. Logowanie/Wylogowanie
        Pierwsze logowanie następuje w opcji rejestracja, każde kolejne po podaniu username i hasła. Dane do logowania są walidowane pod kątem ich poprawności
        Wylogowanie po wciśnięciu przycisku "logout"
    3. Dodawanie postów:
        Opcja dostępna tylko dla zalogowanych użytkowników po wybraniu przycisku 'Dodaj post'
        Edycji postu może dokonywac jedynie autor postu. Opcja usuwania dostępna tylko dla administratora i autora
        Dostępne pola:
            autor - pole wypełniane automatycznie, pobierana wartość "username" zalogowanego użytkonika
            kategoria - pole wyboru, wartość pobierana z tablicy "BlogCategory"
            tagi - pole tekstowe, opcjonalnie uzupełniane przez użytkownika, do 50 znaków
            tytuł - pole tekstowe, obowiązkowo uzupełniane przez użytkownika, do 100 znaków
            skrót - pole tekstowe, obowiązkowo uzupełniane przez użytkownika, do 300 znaków
            pełna treść- pole pozwalające na dodanie teksty i obrazu, obowiązkowo wypełniane przez użytkownika, 
            data utworzenia - pole typu timestamp - uzupełniane automatycznie czasem utworzenia post
            data publikacji - pole typu timestamp, opcjonalnie uzpełniane przez użytkonika
            przycisk wyślij - dodaje post do bazy oraz wysyła na stronę główną 
            przycisk zapisz - dodaje post do bazy  
    4. Dodawanie komentarzy
        Opcja dostępna dla każdego użytkownika, pole aktywne po otawrciu posta. Opcja usuwania komentarzy dostępna tylko dla administratora
        Pole komentarza jest polem tekstowym o długości do 500 znaków
    5. Przeglądanie postów
        opcja dostępna dla każdego użytkownika. 
        Tytuł oraz skrót dostępne na stronie głównej oraz w oknie kategorii postów. Widok pełny z pełną treścią oraz komentarzami widoczy po wejściu w okno postu
        Dostępne pole wyboru kategorii, które przekierowuje do okna z postami w wybranej kategorii
        # poza mvp -Użytkownik ma możliwość wyszukiwania postów po tytule, autorze

### Autorzy
    * Żaneta
    * Patrycja
    * Dawid

### Wymagania
    Wszystkie niezbędne pliki konieczne do uruchomienia projektu zostały umieszczone w pliku requirements.txt.

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
    
    5. Utworzenie superuser:
    
            python manage.py createsuperuser
    
    6. Migracja danych do tabel w bazie:
    
            python manage.py makemigrations
            python manage.py migrate
            
    7. Uruchomienie serwera:
    
            python mamage.py runserver
