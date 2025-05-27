import random
import textwrap
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_age_description(varsta):
    varsta = int(varsta)
    if varsta < 13:
        return random.choice(["copil curajos", "băiat isteț", "fată voioasă"])
    elif varsta < 20:
        return random.choice(["adolescent hotărât", "tânăr ambitios", "tinerel visător"])
    elif varsta < 40:
        return random.choice(["bărbat în putere", "femeie inteligentă", "adult perseverent"])
    elif varsta < 60:
        return random.choice(["om experimentat", "femeie înțeleaptă", "războinic bătrân"])
    else:
        return random.choice(["bătrân înțelept", "moș cu experiență", "bunică iscusită"])

def build_sentence(fragments):
    """Ensure proper grammar by joining sentence fragments correctly"""
    sentence = ' '.join(fragments)
    # Capitalize first letter and add period if missing
    sentence = sentence[0].upper() + sentence[1:]
    if not sentence.endswith(('.','!','?')):
        sentence += '.'
    # Fix common grammar issues
    replacements = [
        (' , ', ', '),
        (' .', '.'),
        (' ;', ';'),
        ('  ', ' '),
        ('pe un ', 'un '),
        ('pe o ', 'o '),
        ('îl ', ''),
        ('o să ', 'să '),
        ('un să ', 'un '),
        ('îi ', 'i '),
        ('își ', 'și ')
    ]
    for old, new in replacements:
        sentence = sentence.replace(old, new)
    return sentence

def generate_paragraph(fragments_list):
    """Generate properly formatted paragraphs"""
    sentences = [build_sentence(fragments) for fragments in fragments_list]
    return ' '.join(sentences)

def genereaza_poveste_random():
    clear_screen()
    print("\n=== GENERATOR DE POVEȘTI AVANSAT ===")
    print("Introdu mai multe detalii pentru o poveste mai complexă!\n")
    
    # Get user input with validation
    nume = input("Numele personajului principal: ").strip()
    while True:
        varsta = input("Vârsta personajului (5-100): ").strip()
        if varsta.isdigit() and 5 <= int(varsta) <= 100:
            break
        print("Vârsta trebuie să fie între 5 și 100!")
    
    trasaturi = []
    while len(trasaturi) < 2:
        trasaturi = [t.strip() for t in input("Trăsături de caracter (minim 2, separate prin virgulă): ").split(',') if t.strip()]
    
    locatie = input("Locul unde se întâmplă povestea: ").strip()
    perioada = input("Perioadă istorică/epocă: ").strip()
    obiect = input("Un obiect magic/important: ").strip()
    scop = input("Scopul personajului principal: ").strip()
    antagonist = input("Numele antagonistului: ").strip()
    
    # Generate story
    story = generate_story(nume, varsta, trasaturi, locatie, perioada, obiect, scop, antagonist)
    
    # Display story
    clear_screen()
    print(story)
    input("\nApasă Enter pentru a închide...")

def generate_story(nume, varsta, trasaturi, locatie, perioada, obiect, scop, antagonist):
    age_desc = get_age_description(varsta)
    gen_poveste = random.choice(["aventură epică", "poveste fantastică", "legendă eroică", "cronică misterioasă"])
    
    # Chapter 1: Beginning
    chapter1 = [
        generate_paragraph([
            [f"În {locatie}, în perioada {perioada}, trăia {nume}, {age_desc} cu {random.choice(trasaturi)}"],
            [f"Viața sa liniștită s-a schimbat când a descoperit {obiect}"],
            [f"Legenda spune că {obiect} poate {random.choice(['schimba soarta lumii', 'acorda puteri nemărginite', 'cheama forțe uitate'])}"]
        ]),
        generate_paragraph([
            [f"{antagonist}, {random.choice(['vrăjitorul cel rău', 'conducătorul întunecat', 'străinul misterios'])}"],
            [f"a aflat despre existența {obiect} și a pornit să-l cucerească"],
            [f"{nume} a fost nevoit să plece într-o călătorie periculoasă"]
        ])
    ]
    
    # Chapter 2: Development
    chapter2 = [
        generate_paragraph([
            [f"După {random.choice(['săptămâni', 'luni', 'ani'])} de călătorie"],
            [f"{nume} a ajuns în {random.choice(['pădurea bântuită', 'orașul uitat', 'munții interzisi'])}"],
            [f"Aici a întâlnit {random.choice(['un înțelept bătrân', 'o vrăjitoare bună', 'un grup de războinici'])}"]
        ]),
        generate_paragraph([
            [f"Aceștia i-au explicat că {obiect} {random.choice(['are un preț teribil', 'cere un sacrificiu', 'poate fi controlat doar cu inima curată'])}"],
            [f"{nume} a învățat să {random.choice(['folosească', 'protejeze', 'înțeleagă'])} {obiect}"]
        ]),
        generate_paragraph([
            [f"În timp ce se pregătea pentru confruntarea finală"],
            [f"{antagonist} a {random.choice(['atacat', 'blocat', 'închis'])} {random.choice(['drumurile', 'porțile', 'calea'])}"],
            [f"lăsându-l pe {nume} să {random.choice(['se descurce singur', 'găsească o soluție creativă', 'își depășească limitele'])}"]
        ])
    ]
    
    # Chapter 3: Climax
    chapter3 = [
        generate_paragraph([
            [f"Confrunatrarea finală a avut loc {random.choice(['sub o ploaie torențială', 'pe vârful unui munte', 'în inima unui vulcan'])}"],
            [f"{nume} și {antagonist} s-au luptat {random.choice(['cu spade', 'cu magie', 'cu vorbe puternice'])}"]
        ]),
        generate_paragraph([
            [f"În momentul decisiv, {nume} a {random.choice(['înțeles', 'simțit', 'văzut'])}"],
            [f"că {random.choice(trasaturi)} era cheia {random.choice(['victoriei', 'supraviețuirii', 'păcii'])}"]
        ])
    ]
    
    # Final Chapter
    final_chapter = [
        generate_paragraph([
            [f"După ce {antagonist} a fost {random.choice(['înfrânt', 'transformat', 'alungat'])}"],
            [f"{obiect} a {random.choice(['strălucit pentru ultima oară', 'dispărut în negură', 'fost înapoiat zeilor'])}"]
        ]),
        generate_paragraph([
            [f"{nume} s-a întors acasă"],
            [f"dar {locatie} nu a mai fost niciodată la fel"],
            [f"Povestea sa a rămas în amintirea oamenilor ca {random.choice(['o lecție', 'o inspirație', 'o avertizare'])}"]
        ])
    ]
    
    # Format the story
    wrapper = textwrap.TextWrapper(width=80)
    story_lines = []
    
    # Header
    story_lines.append("="*80)
    story_lines.append(f"POVESTEA LUI {nume.upper()} ȘI {obiect.upper()}".center(80))
    story_lines.append(f"Gen: {gen_poveste.title()} | Locatie: {locatie} | Perioada: {perioada}".center(80))
    story_lines.append("="*80 + "\n")
    
    # Chapter 1
    story_lines.append("CAPITOLUL 1: ÎNCEPUTURI".center(80, '-'))
    for para in chapter1:
        story_lines.extend(wrapper.wrap(para))
        story_lines.append("")
    story_lines.append("")
    
    # Chapter 2
    story_lines.append("CAPITOLUL 2: DEZVOLTARE".center(80, '-'))
    for para in chapter2:
        story_lines.extend(wrapper.wrap(para))
        story_lines.append("")
    story_lines.append("")
    
    # Chapter 3
    story_lines.append("CAPITOLUL 3: CLIMAX".center(80, '-'))
    for para in chapter3:
        story_lines.extend(wrapper.wrap(para))
        story_lines.append("")
    story_lines.append("")
    
    # Final Chapter
    story_lines.append("CAPITOLUL FINAL: ÎNCHEIERE".center(80, '-'))
    for para in final_chapter:
        story_lines.extend(wrapper.wrap(para))
        story_lines.append("")
    story_lines.append("")
    
    # Footer
    story_lines.append("="*80)
    story_lines.append("SFÂRȘIT".center(80))
    story_lines.append("="*80)
    
    return '\n'.join(story_lines)

if __name__ == "__main__":
    genereaza_poveste_random()