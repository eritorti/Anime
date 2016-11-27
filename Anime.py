def anime():
    print('!!!Wenn sie ihren einen Anime gefunden haben,geben sie ihn ein,für mehr Informationen!!!','\n')
    print('Es gibt folgende Genre zu ihrer auswahl:','\n'*3,' '*5,'Thriller','\n',' '*5,'Action','\n',' '*5,'Romance','\n',' '*5,'Mystery','\n',' '*5,'Ninja','\n',' '*5,'Fantasy','\n',' '*5,'Krimi','\n',' '*5,'Shounen(Langzeit)','\n')
    k=input('Wählen sie bitte ein Genre aus.:')
    k2=input('Wählen sie bitte ihr zweites Genre aus.:')
    k3=input('Wählen sie bitte ihr drittes Genre aus(falls vorhanden).:')

    if(k=='Action' and k2=='Thriller' and k3=='Mystery' or k=='Thriller' and k2=='Action' and k3=='Mystery' or k=='Mystery' and k2=='Action' and k3=='Thriller' or k=='Action' and k2=='Mystery' and k3=='Thriller' or k=='Mystery' and k2=='Thriller' and k3=='Action' or k=='Thriller' and k2=='Mystery' and k3=='Action'):
        print('\n'*2,' '*5,'Mirai_Nikki')
        print('\n'+'Wenn sie die Musik hören möchten geben sie bitte "MRsong()" ein,dann werden sie auf eine Internet seite weitergeleitet(Es werden sich zewi Tabs öffnen das Opening und das Theme).')
        print('\n'+'Wenn sie den Trailer sehen möchten geben sie bitte "MRtrailer()" ein,dann werden sie auf eine Internet seite weitergeleitet.')
              
    elif(k=='Ninja' and k2=='Shounen' and k3=='Action' or k=='Ninja' and k2=='Action' and k3=='Shounen' or k=='Shounen' and k2=='Action' and k3=='Ninja' or k=='Shounen' and k2=='Ninja' and k3=='Action' or k=='Action' and k2=='Ninja' and k3=='Shounen' or k=='Action' and k2=='Shounen' and k3=='Ninja'):
        print('\n'*2,' '*5,'Naruto','\n',' '*5,'Naruto_Shippuuden')
        print('\n'+'Wenn sie die Musik hören möchten geben sie bitte "NSsong()" ein,dann werden sie auf eine Internet seite weitergeleitet.')
        print('Wenn sie den Trailer sehen möchten geben sie bitte "NStrailer()" ein,dann werden sie auf eine Internet seite weitergeleitet.')
              
    elif(k=='Romance' and k2=='Action' and k3=='Fantasy' or k=='Romance' and k2=='Fantasy' and k3=='Action' or k=='Action' and k2=='Romance' and k3=='Fantasy' or k=='Action' and k2=='Fantasy' and k3=='Romance' or k=='Fantasy' and k2=='Romance' and k3=='Action' or k=='Fantasy' and k2=='Action' and k3=='Romance'):
        print('\n'*2,' '*5,'Sword_Art_Online')
        print('\n'+'Wenn sie die Musik hören möchten geben sie bitte "SAOsong()" ein,dann werden sie auf eine Internet seite weitergeleitet.')
        print('\n'+'Wenn sie den Trailer sehen möchten geben sie bitte "SAOtrailer()" ein,dann werden sie auf eine Internet seite weitergeleitet.')

    elif(k=='Krimi' and k2=='Thriller' and k3=='' or k=='Thriller' and k2=='Krimi' and k3==''):
        print('\n'*2,' '*5,'Death_Note')
        print('\n'+'Wenn sie die Musik hören möchten geben sie bitte "DNsong()" ein,dann werden sie auf eine Internet seite weitergeleitet.')
        print('\n'+'Wenn sie den Trailer sehen möchten geben sie bitte "DNtrailer()" ein,dann werden sie auf eine Internet seite weitergeleitet.')
              
    elif(k=='Fantasy' and k2=='Action' and k3=='Shounen' or k=='Fantasy' and k2=='Shounen' and k3=='Action' or k=='Action' and k2=='Fantasy' and k3=='Shounen' or k=='Action' and k2=='Shounen' and k3=='Fantasy' or k=='Shounen' and k2=='Fantasy' and k3=='Action' or k=='Shounen' and k2=='Action' and k3=='Fantasy'):
        print('\n'*2,' '*5,'Fairy_Tail')
        print('\n'+'Wenn sie die Musik hören möchten geben sie bitte "FTsong()" ein,dann werden sie auf eine Internet seite weitergeleitet.')
        print('\n'+'Wenn sie den Trailer sehen möchten geben sie bitte "FTtrailer()" ein,dann werden sie auf eine Internet seite weitergeleitet.')
              
    elif(k=='Fantasy' and k2=='Action' and k3=='' or k=='Action' and k2=='Fantasy' and k3==''):
        print('\n'*2,' '*5,'Fate_Zero')
        print('\n'+'Wenn sie die Musik hören möchten geben sie bitte "FZsong()" ein,dann werden sie auf eine Internet seite weitergeleitet.')
        print('\n'+'Wenn sie den Trailer sehen möchten geben sie bitte "FZtrailer()" ein,dann werden sie auf eine Internet seite weitergeleitet.')

    elif(k=='Adventure' and k2=='Fantasy' and k3=='' or k=='Fantasy' and k2=='Adventure' and k3==''):
        print('\n'*2,' '*5,'Fullmetall_Alchemist','\n',' '*5,'Fullmetall_Alchemist_Brotherhood')
        print('\n'+'Wenn sie die Musik hören möchten geben sie bitte "FABsong()" ein,dann werden sie auf eine Internet seite weitergeleitet.')
        print('\n'+'Wenn sie den Trailer sehen möchten geben sie bitte "FAtrailer" ein,dann werden sie auf eine Internet seite weitergeleitet.')
              
    elif(k=='Drama' and k2=='' and k3==''):
        print('\n',' '*5,'Elfen_Lied')
        print('\n'+'Wenn sie die Musik hören möchten geben sie bitte "ELsong()" ein,dann werden sie auf eine Internet seite weitergeleitet.') 
        print('\n'+'Wenn sie den Trailer sehen möchten geben sie bitte "ELtrailer()" ein,dann werden sie auf eine Internet seite weitergeleitet.')

    else:
        print('\n'*2+'Es konnte kein genaues ergebniss gefunden werden.Geben sie "Help()" für mehr Informationen ein.')

def MRsong():
    import webbrowser
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=FpSu77yl5W0")
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=09r-78dfrvc")
def NSsong():
    import webbrowser
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=FNTD6miTjRM")
def SAOsong():
    import webbrowser
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=_w8jFwec0B8")
def DNsong():
    import webbrowser
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=UkZVOpb-zPA")
def FTsong():
    import webbrowser
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=kIwmrk7LoDk")
def FZsong():
    import webbrowser
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=8mK_0up-LMc")
def FABsong():
    import webbrowser
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=SkNjCfMjRXA")
def ELsong():
    import webbrowser
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=kua_iJ4bAmo")
def MRtrailer():
    import webbrowser
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=aoBHx0pPlWY&t=9s")
def NStrailer():
    import webbrowser
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=XBJEiovuOgc")   
def SAOtrailer():
    import webbrowser
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=6ohYYtxfDCg")
def DNtrailer():
    import webbrowser
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=Slh-VW8QsT8")
def FTtrailer():
    import webbrowser
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=R6ZbNo4H-IM")
def FZtrailer():
    import webbrowser
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=Kgg201KkzaY")
def FABtrailer():
    import webbrowser
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=NqXH2oRsGpA&t=13s")
def ELtrailer():
    import webbrowser
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=cjetz2UCBK4")
def Help():
    print('Falls kein Anime gefunden werden konnte,versuchen sie es erneut aber achten sie auf Groß-kleinschreibung.Oder es gibt ,bei uns,keinen Anime der diese Kriterien erfüllt.','\n'*2+'Falls das programm nicht richtig ausgeführt wird,benachrichtigen sie uns bitte unter "xariking@gmail.com".','\n'*2+'Falls sie anregungen haben teilen sie uns diese mit unter "xariking@gmail.com".')


Mirai_Nikki='Den Highschoolschüler Yukiteru Amano plagt das Gefühl der Einsamkeit. Einzig das imaginäre Wesen Deus Ex Machina leistet Yukiteru Gesellschaft und erklärt diesem, dass er der Gott von Raum und Zeit sei. Deus Ex Machina modifiziert Yukiterus Handy um, so dass es die Zukunft seines Besitzers in Form eines Tagebuchs voraussagt. Doch nachdem Yukiteru der Besitzer des neuen Handys wird, muss er zusammen mit 11 anderen Auserwählten an einem Spiel auf Leben und Tod teilnehmen, um am Ende der Nachfolger von Deus Ex Machina zu werden.'
Naruto='Ein riesiges neunschwänziges Fuchsmonster greift das Dorf Konohagakure an und zerstört alles in seiner Umgebung.Viele tapfere Ninjas sterben bei dem Versuch ihre Familien zu beschützen und das Dorf zu verteidigen. Schließlich schafft es ein einzigartiger Ninja den Dämon zu bändigen und schließt ihn in den Körper eines Neugeborenen ein. Jedoch muss dieser Held, der Hokage der vierten Generation, einen hohen Preis zahlen. Er verliert sein Leben bei der Rettung des Dorfes. 12 Jahre sind nach diesem Unglück vergangen, der Junge Naruto Uzumaki, ein etwas tollpatschiger Ninja, hat gerade seine erste Abschlussprüfung an der Ninja-Akademie bestanden. Nachdem er nun die erste Hürde auf dem Weg ein großer Ninja zu werden bestanden hat, macht er sich mit seinen beiden Freunden auf, um viele Missionen für das Dorf zu erledigen.'
Naruto_Shippuuden='Der japanische Anime "Naruto Shippuden" knüpft an die Serie „Naruto“ an und begleitet Naruto Uzumaki auf seiner Reise, Hokage (Dorfoberhaupt) von Konohagakure zu werden. Er erhofft sich dadurch den Respekt der anderen, der ihm früher versagt geblieben ist. Deswegen versucht er mit allen Mitteln die Freundschaft zwischen Sasuke Uchiha und ihm am Leben zu erhalten obwohl er ihn als sehr großen Rivalen ansieht. Dieser hat es sich jedoch zum Ziel gemacht seinen Bruder Itachi zu ermorden und dafür wendete er sich von seinen Freunden ab und dem Bösen zu, um mehr Macht und Stärke zu erlangen. Naruto und Sakura, die dritte im früheren Team, geben ihn aber nicht auf und versuchen ihn immer wieder zur Umkehr zu bewegen.'
Sword_Art_Online='Kazuto Kirigaya testet als einer der ersten einen neuen Hightech-Helm, welcher die Psyche des Nutzers komplett in die Welt des MMORPGs „Sword Art Online“ transferiert. Als Tester der Beta-Version besitzt er bereits einiges an Erfahrung und kämpfte sich mehr als erfolgreich als „Kirito“ durch die ersten Ebenen der Fantasy-Welt. Doch schon kurz nach der Eröffnung SAOs merken die Spieler, dass etwas nicht stimmt: Im Menü gibt es keinen Logout-Button. Hinter dem Grund der allgemeinen aufkommenden Panik scheint der Administrator des Spiels zu stecken und die einzige Möglichkeit wieder in die reale Welt zurückzukehren besteht darin, SAO erfolgreich abzuschließen. Doch das ist leichter gesagt als getan, denn der Tod in der Fantasy-Welt bedeutet auch den richtigen Tod in der richtigen Welt.Doch zu seinem Glück muss er die Welt nicht alleine bestreiten...'
Death_Note='Light Yagami steht kurz vor der Aufnahmeprüfung für Japans Elite-Universitäten, doch als er auf dem Schulhof ein rätselhaftes Notizbuch findet, wird sein Gerechtigkeitssinn auf die Probe gestellt. Das Buch entpuppt sich als "Death Note", das Buch eines japanischen Todesgottes, das seinem Benutzer die Macht verleiht, jede Person, die er in es hineinschreibt, zu töten. Nach anfänglicher Skepsis findet Light heraus, dass das "Death Note" tatsächlich funktioniert, indem er es an einem Kriminellen testet. Light sieht das "Death Note" als Chance, um die Welt vom Verbrechen zu befreien, indem er die Namen sämtlicher, bekannter Straftäter notiert. Doch bleiben seine Taten nicht lange unbemerkt. Die Anzahl unerklärlicher Tode erregt nicht nur die Aufmerksamkeit der Polizei, sondern auch die des mysteriösen, weltweit als "L" bekannten Sonderermittlers.'
Fairy_Tail='Eine von Magie durchdrungene Welt, in der Zauberei noch alltäglich ist... beherrscht von mächtigen Magiergilden, die für Recht und Ordnung sorgen... und zuweilen auch etwas übertreiben...?! FAIRY TAIL ist eine dieser Gilden. Laut, zerstörerisch, immer feiernd und stets für einen Kampf zu haben, zählt diese Gemeinschaft einige der mächtigsten Magier dieser Zeit zu ihren Reihen. Die junge Lucy lernt ihre neue Gilde sowie deren Mitglieder schnell zu schätzen: den draufgängerischen Feuermagier Natsu mit seiner sprechenden Katze Happy, den coolen Eismagier Gray, die unerschrockene Erza, den kleinwüchsigen alten Meister Makarov und, und, und... Doch es herrscht nicht immer Harmonie in der Magierwelt: dunkle Gilden und arkane Mächte bedrohen die Ordnung - gut, wenn man sich auf seine Freunde verlassen kann!'
Fate_Zero='Dies ist die Geschichte der Stunde null, des Anfangs. Der ultimative Kampf zwischen 7 Großmeistern und ihren mystischen Dienern, um die Herrschaft über den Heiligen Gral. Nach drei Kriegen ohne klaren Sieger geht es nun in die vierte Runde. Die Magier eilen zum Schlachtfeld in Fuyuki, jeder mit seinen eigenen Wünschen und Hoffnungen. Einer unter ihnen sieht jedoch keinen Sinn in dem Gralskrieg. Sein Name ist Kirei Kotomine. Unfähig den Plan, den das Schicksal für ihn bereit hält, zu verstehen, ist Kirei permanent von Zweifeln und Ungewissheit geplagt. Warum wurde gerade er mit einem der begehrten Kommando-Siegel ausgestattet?'
Fullmetall_Alchemist_Brotherhood='In dieser Welt existiert eine Kraft, die grenzenlos erscheint. Alchemie, auch bekannt als die Grundlage dieser Welt, funktioniert unter dem Prinzip des äquivalenten Tausches. Um einen Gegenstand zu erhalten, muss etwas anderes mit dem selben Wert dafür eingetauscht werden. Manche nennen es eine Wissenschaft, andere Magie und wiederum andere glauben, es wäre ein Wunder. Aber egal wie mächtig Alchemie auch sein mag, sie hat trotzdem Grenzen, die nicht überschritten werden dürfen. Die Gebrüder Elric verloren ihre Mutter und brachen daraufhin das größte Tabu der Alchemie: Die Menschliche Transmutation. In Folge dessen verlor der ältere Bruder Edward Elric seinen rechten Arm und sein linkes Bein. Der jüngere Bruder hingegen seinen ganzen Körper und ist nun an einer Rüstung gebunden. Zusammen machen sie sich auf den weg um ihre Körper wieder zu erlangen. Dabei treffen sie sowohl gute Freunde als auch grausame Feinde.'
Fullmetall_Alchemist='Die Alchemisten Edward Elric und sein jüngerer Bruder, der seit einem Vorfall in einer Rüstung gefangen ist, suchen nach dem Stein der Weisen und reisen dafür durch eine Welt, in der das Militär die oberste Ordnung darstellt. Dass diese Art von Regierung, obwohl sie einen anderen Anschein erweckt, nicht wirklich gerecht handelt, sollen beide erst im Verlauf ihrer Reise, auf welcher dies ihre geringste Sorge sein wird, herausfinden.'
Elfen_Lied='Den Kern der Story bilden die "Diclonius", sie scheinen die nächste Stufe der Evolution zu sein. Es sind Wesen mit hornähnlichen Verformungen an ihren Köpfen. Sie besitzen starke telekinetischen Kräfte, die sich in Form von unsichtbaren Armen ausbilden. Mit diesen Kräften könnten sie mit Leichtigkeit die Menschheit ausrotten.Eines Tages kann eine der Diclonius entkommen (Lucy). Auf ihrer Flucht schlägt sie sich eine blutige Schneise durch die Reihen der Wachmänner. Sie wird jedoch zum Schluss schwer am Kopf verletzt, stürzt ins Meer und als sie wieder zu sich kommt, hat sie ihr Gedächtnis verloren und ist wieder so unschuldig wie ein Kind. Lucy wird von Kouta und Yuka an einem Strand aufgelesen. Von Kouta und Yuka wird sie von nun an Nyuu genannt, da sie nichts anderes mehr sagen kann als eben „Nyuu“. Von da an leben diese drei zusammen in einem Haus ohne von den drohenden Gefahren zu wissen, die auf sie noch lauern werden.'




