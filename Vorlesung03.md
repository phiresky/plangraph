> (Beginn Vorlesung 2015-04-29)

# Färbung planarer Graphen (Kap.4 im Skript; "Listenfärbung" nicht im Skript, aber Folien)

## Färbungsproblem (k-Färbung)

__geg.__ $G=(V,E)$, k Farben

__Problem__ Existiert _korrekte_ Färbung der Knoten aus V mit diesen k Farben, d.h. falls $\{u,v\} \in E \implies Farbe(u) \neq Farbe(v)$

## Listenfärbungsproblem

__geg.__ $G=(V,E), k \in ℕ$

__Problem__ Gibt es für _jede_ Zuordnung von Listen $S_v$ zu Knoten $v\in V$ mit $|S_v|=k$ eine korrekte Färbung der Knoten bei der jeder Knoten eine Farbe aus seiner Liste enthält?


__Beobachtung__ Listenfärbung ist Verallgemeinerung von Färbungsproblem.

__Satz__ Jeder planare Graph ist 5-listenfärbbar.

__Beweis__ Induktion über $|V|=n$ (benutzen nicht, dass v exist. mit $d(v)\leq 5$).

beweisen schärfere Behauptung:

Falls G planar und

- jede innere Facette Dreieck
- äußere Facette durch Kreis $C=v_1 v_2 \dots v_k v_1$ begrenzt
- $v_1$ mit Farbe 1 gefärbt
- $v_2$ mit Farbe 2 gefärbt
- jeder Knoten mit Liste von mind. 3 Farben assoziiert
- jeder Knoten aus $G-C$ mit Liste von mind. 5 Farben assoziiert

dann folgt: G korrekt färbbar

Offensichtlich folgt daraus 5-Listenfärbbarkeit.

### Beweis der schärferen Behauptung per Induktion

Falls $G=(V,E)$ planar und $|V|=3$ trivial

__Induktionsschritt__ $G=(V,E)$ pl. und $|V|\geq 4$, Kreis C der äußeren Facette begrenzt

zwei Fälle: C enthält Sehne $\{v,w\}$ im Inneren oder nicht

*(todo: bild)*

#### Fall 1: C enthält Sehne $\{v,w\}$

$\{v,w\}$ induziert eindeutig bestimmte Kreise $C_1$ und $C_2$ welche jeweils Subproblem $G_1$ und $G_2$ induzieren. o.B.d.A. enthalte $C_1$ Kante $\{v_1,v_2\}$ (und damit $v_1,v_2$ nicht beide auf $C_2$. Wende IV auf $C_1$ an und dann IV auf $C_2$ wobei v und w Rolle von $v_1,v_2$ spielen. ⇒ Färbung von $G_1$ und $G_2$ ind. korrekte Färbung von G.

#### Fall 2: C enthält keine Sehne

Seien $v_{k-1},u_1,u_2,\dots u_l,v_1$ die Nachbarn von $v_k$. Da alle inneren Facetten Dreiecke ist $v_{k-1} u_1 \dots u_l v_1$ Weg P und $(C-v_k) \cup P = C'$ wird Kreis der äußere Facette begrenzt. "Reserviere" zwei Farben aus Liste von $v_k$ und entferne diese ggf. aus Listen von $u_1,\dots,u_l$. Wende IV auf durch $C'$ induz. Graph an. Höchstens eine der beiden reservieten Farben wird für $v_{k-1}$ verwendet, die andere kann für $v_k$ verwendet werden.

#### Satz

Nicht jeder planare Graph ist 4-listenfärbbar.

#### Beweis

konst. Gegenbeispiel, d.h. planarer Graph mit Listenzuweisung mit Listen $S_v,|S_v|=4$, so dass Graph nicht korrekt färbbar unter Berücksichtigung der $S_v$.

Kern der Konstruktion:

*(todo: bild)*

hat "vis-à-vis-Eigenschaft", d.h. in korrekte Färbung müssen mind. zwei gegenüberliegende Eckknoten dieselbe Farben haben. (klar!)


---
