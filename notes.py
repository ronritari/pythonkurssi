import time
import pickle

def load_notes():
    try:
        with open("muistio.dat", "rb") as file:
            notes = pickle.load(file)
        print("Muistio ladattu.")
    except FileNotFoundError:
        notes = []
        print("Virhe tiedostossa, luodaan uusi muistio.dat.")
    return notes

def save_notes(notes):
    with open("muistio.dat", "wb") as file:
        pickle.dump(notes, file)
    print("Muistio tallennettu.")

def print_notes(notes):
    print("Muistion sisältö:")
    for i, note in enumerate(notes):
        print(f"{i+1}. {note}")

def add_note():
    note = input("Kirjoita uusi merkintä: ")
    timestamp = time.strftime("%X %x")
    return f"{note}:::{timestamp}"

def edit_note(notes):
    #print_notes(notes)
    print(f"Listalla on {len(notes)} merkintää.")
    note_index = int(input("Mitä niistä muutetaan?: "))-1
    notes.pop(note_index)
    print_notes(notes)
    if 0 <= note_index < len(notes):
        new_note = input("Anna uusi teksti: ")
        timestamp = time.strftime("%X %x")
        notes[note_index] = f"{new_note}:::{timestamp}"
    else:
        print("Virheellinen merkinnän numero.")

def delete_note(notes):
    print_notes(notes)
    print(f"Listalla on {len(notes)} merkintää.")
    note_index = int(input("Mitä niistä poistetaan?: ")) - 1
    if 0 <= note_index < len(notes):
        deleted_note = notes.pop(note_index)
        print(f"Poistettiin merkintä {deleted_note}")
    else:
        print("Virheellinen merkinnän numero.")

def main():
    notes = load_notes()
    while True:
        print("\n(1) Lue muistikirjaa")
        print("(2) Lisää merkintä")
        print("(3) Muokkaa merkintää")
        print("(4) Poista merkintä")
        print("(5) Tallenna ja lopeta")

        choice = input("Mitä haluat tehdä?: ")
        if choice == "1":
            print_notes(notes)
        elif choice == "2":
            new_note = add_note()
            notes.append(new_note)
        elif choice == "3":
            edit_note(notes)
        elif choice == "4":
            delete_note(notes)
        elif choice == "5":
            save_notes(notes)
            print("Lopetetaan.")
            break
        else:
            print("Virheellinen valinta.")

if __name__ == "__main__":
    main()
