---
title: Mitschrieb Planare Graphen SS 2015
author: Robin
papersize: a4paper
header-includes:
    - \usepackage{unicode-math}
	- \usepackage{mathtools}
include-before:
    - \input{fixunicode.tex}

---
> 2015-04-15 

# Grundlegende Eigenschaften planarer Graphen

## planare Einbettung:
Graph $G = (V,E)$ kann dargestellt werden indem man die Knoten aus V auf Punkte im $ℝ²$ und die Kanten aus E auf Jordan-Kurven (d.h. stetige sich selbst nicht kreuzende Kurven) zwischen den Endpunkten abdeckt.

G heißt _planar_ wenn es eine Darstellung gibt, bei der sich die Kanten höchstens in einem gemeinsamen Endpunkt berühren.

- planare Einstellung zerlegt Ebene in _Facetten_ (Gebiete, Flächen)
- planare Einbettung, die durch ihre Facetten bzw. die Reihenfolge der Kanten in Adjazenzlisten beschrieben ist, heißt _kombinatorische Einbettung_
- planare Einbettung, die durch Koordinaten der Punkte beschrieben ist, heißt _geometrische Einbettung_

Facettenmenge $\mathcal{F}$, $|\mathcal{F}| = f$

## Satz von Euler (1790):

In einem zusammenhängenden nichtleeren planaren Graph $G=(V,E)$ gilt für jede planare Einbettung (geg. durch $\mathcal{F}$), dass $$n-m+f=2$$ (wobei $|V|=n, |E|=m, |\mathcal{F}| = f$)

__Beweis__ per Induktion über m:

__IA__: $m=0$, es ist $n=1, f=1$ ⇒ Beh.

Sei also m ≥ 1

_Fall 1:_ G enthalte einen Kreis

⇒ es existiert $l \in E$ so dass $G':= G - e = (V, E \setminus e)$ ebenfalls zusammenhängend und e an zwei Facetten grenzt die zu einer Facette in G' werden.

⇒ f' #Facetten von G' erfüllt $$ f' = f - 1 \underset{IV}{\implies} n - (m-1) + f' = 2$$ $$\implies n-m+f = 2 $$

_Fall 2:_ G enthält keinen Kreis, ist also Baum und $|\mathcal{F}| = 1$ . Für beliebige $e \in E$ zerfällt $G' = G - e$ in zwei Zusammenhangskomponenten $G_1 = (V_1, E_2)$ und $G_2 = (V_2, E_2)$ und nach IV: $$n_1 - m_1 + f_1 = 2, n_2 - m_2 + f_2 = 2$$

Da $$ n=n_1 + n_2, m=m_1 + m_2 - 1 $$$$ \implies n-m+f = n_1 + n_2 - m_1 - m_2 - 1 +1 = \equalto{(n_1 - m_1 + 1)}{2}+\equalto{(n_2-m_2 + 1)}{2} - 2 = 2$$

__Folgerungen:__

- \#Facetten ist für jede planare Einbettung von G gleich
- \#Kanten eines Baumes mit n Knoten ist n-1

_Lemma:_ Ein planarer Graph mit n Knoten ($n \geq 3$) hat höchstens $3n - 6$ Kanten.

_Beweis:_ o.B.d.A sei G maximal planar (d.h. Hinzunahme weiterer Kanten zerstört Planarität)

`Bild`

Dann ist für jede planare Einbettung jede Facette ein Dreieck und jede Kante grenzt an genau zwei Facetten.

$$ 3 f = 2 m $$
$$ \underset{mit~Euler}{=} $$
$$ 3 (2-n+m) = 6-3n+3m $$

_Lemma:_ Sei G pl. Graph mit mind 3 Knoten. $d_{max}(G)$ bezeichne Maximalgrad in G, $n_i$ \#Knoten von Grad i.

Dann gilt: $$6n_0 + 5n_1 + 4n_2 + 3n_3 + 2n_4 + n_5 \geq n_7 + 2n_8 + 3n_9 + \dots + (d_{max}(G) - 6) * n_{d_{max}(G)} + 12$$

_Beweis:_ Es gilt $n = \sum_{i=0}^{d_{max}(G)} n_i$ und $2m=\sum_{i=0}^{d_{max}(G)} i \cdot n_i.$

Da $m \leq 3n - 6$ folgt $$6 \sum_{i=0}^{d_{max}(G)}  n_i = 6n \geq 2m + 12 = \sum_{i=0}^{d_{max}(G)} i \cdot n_i + 12$$

_Folgerung:_ Jeder planare Graph enthält mind. einen Knoten v mit $d(v) \leq 5$.

---

## Dualität von Schnitten und Kreisen

`Bild Dualgraph`

Planarer Graph G mit Einbettung $\mathcal{F}_i$ Dualgraph $G^*$ dazu. Dann gilt:

Ein Schnitt  in G ($\widehat{=}$ entspr. Kantenmenge) induziert eine Menge von Kreisen in $G^*$ und umgekehrt.

## Minor bzw. Unterteilung

`Bild G' Subgraph von G`

$G' = (V', E')$ heißt _Subgraph_ von $G=(V,E)$ wenn $V'\subseteq V$ und $E' \subseteq E$.

$G'=(V',E')$ heißt _Unterteilung_ von $G=(V,E)$ wenn $G'$ aus $G$ entsteht indem man Kanten von G durch einfache Wege ersetzt.

Ein Graph H heißt _Minor_ von G wenn H aus G entsteht durch Löschen von Knoten oder/und Kanten und/oder Knotenkontraktion von Knoten von Grad 2.

H ist _Minor_ von G falls G eine Unterteilung von H als Subgraph enthält.

`Bild G' Unterteilung von G`

`Bild G' Minor von G`

## Satz von Kuratowski (1930)

Ein Graph $G=(V,E)$ ist genau dann planar wenn er weder $K_5$ noch $K_{3,3}$ als Minor enthält.

"⇒" klar, da $K_5$ und $K_{3,3}$ nicht planar.

"⇐": Es ist also "nur" zu zeigen: Wenn G nicht planar, dann enthält G einen $K_5$ oder $K_{3,3}$ als Minor.

### Vorbereitung des Beweises

`Bild K_{3,2}`

Nehme Graph der $K_{3,2}$ als Minor enthält θ-Graph (θ Minor von $K_{3,2}$)


> (2014-04-21)

Siehe Beweisfolien (kuratowski_slides.pdf)

> (2014-04-29)

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

`bild`

#### Fall 1: C enthält Sehne $\{v,w\}$

$\{v,w\}$ induziert eindeutig bestimmte Kreise $C_1$ und $C_2$ welche jeweils Subproblem $G_1$ und $G_2$ induzieren. o.B.d.A. enthalte $C_1$ Kante $\{v_1,v_2\}$ (und damit $v_1,v_2$ nicht beide auf $C_2$. Wende IV auf $C_1$ an und dann IV auf $C_2$ wobei v und w Rolle von $v_1,v_2$ spielen. ⇒ Färbung von $G_1$ und $G_2$ ind. korrekte Färbung von G.

#### Fall 2: C enthält keine Sehne

Seien $v_{k-1},u_1,u_2,\dots u_l,v_1$ die Nachbarn von $v_k$. Da alle inneren Facetten Dreiecke ist $v_{k-1} u_1 \dots u_l v_1$ Weg P und $(C-v_k) \cup P = C'$ wird Kreis der äußere Facette begrenzt. "Reserviere" zwei Farben aus Liste von $v_k$ und entferne diese ggf. aus Listen von $u_1,\dots,u_l$. Wende IV auf durch $C'$ induz. Graph an. Höchstens eine der beiden reservieten Farben wird für $v_{k-1}$ verwendet, die andere kann für $v_k$ verwendet werden.

#### Satz

Nicht jeder planare Graph ist 4-listenfärbbar.

#### Beweis

konst. Gegenbeispiel, d.h. planarer Graph mit Listenzuweisung mit Listen $S_v,|S_v|=4$, so dass Graph nicht korrekt färbbar unter Berücksichtigung der $S_v$.

Kern der Konstruktion:

`bild`

hat "vis-à-vis-Eigenschaft", d.h. in korrekte Färbung müssen mind. zwei gegenüberliegende Eckknoten dieselbe Farben haben. (klar!)


---

> 2015-05-12

Bemerkung zu Planar Separator Theorem: Linearzeitimplementierung

PST: pl. $G=(V,E);$ exist Separator S der G in $G_1=(V_1,E_1), G_2=(V_2,E_2)$ trennt mit

1. $|V_1|,|V_2| \leq {2 \over 3} n$
2. $|s| \leq 4 \sqrt{n}$


# Matching

$G=(V,E)$, ein Matching $M \subseteq E$ sodass keine zwei Kanten aus M gemeinsame Endknoten haben.

$w:E\to\mathbb{R}$

- Finde $M \subseteq E$ _Matching mit max. Gewicht_, wobei $w(m)=\sum_{l \in M} w(l)$
- Finde $M \subseteq E$ _Matching mit max. Kardinalität_, (Fall w(l) = 1 f.a. $l \in E$

Beide Probleme sind auch für bel. Graphen in P.

`bild`

alternierender Weg bzgl. M → Vertauschen der Kanten auf Weg aus M mit Kanten auf Weg, die nicht in M sind resultiert in größerem Matching M*

---

- Ein bezüglich einem Matching M _alternierender Weg_ ist ein einfacher Weg oder einfach Kreis, dessen Kanten abwechselnd in M und $E\setminus M$ sind.
- Alternierender Weg P (bezeichne entsprechende Kantenmenge) ist _erhöhender Weg_ falls $$\sum_{l \in P, l \in E \setminus M} w(l) > \sum_{l \in P, l \in M} w(l)$$ und P entweder Kreis (gerader Länge) oder dessen erste und letzte Kante beide in M sind oder inzident zu einem ungematchten Knoten.

#### Beobachtung

M Matching, P erhöhender Weg bzgl M ⇒ $M'=(M\setminus P) \cup (P\setminus M)$ wieder Matching mit $w(M')>w(M).$

#### Lemma

$G=(V,E), w:E\to \mathbb{R}$, M Matching in G. Dann ist $w(M)$ maximal genau dann wenn es keinen erhöhenden Weg bzgl. M gibt.

#### Beweis

"⇒" klar

"⇐" sei M nicht max. Matching in G und es existiert kein bzgl. M erhöhender Weg. Dann exist. Matching $M^*$ mit $w(M^*) > w(m)$. Betrachte Subgraph $G_{M^*\triangle M}$ von G der durch $$M^*\triangle M = M \cup M^* \setminus(M\cap M^*)$$ induziert wird. In diesem Graph haben alle Knoten Grad 1 und Grad 2 und er besteht aus einfachen Wegen und Kreisen.  
Falls kein Kreis in $G_{M\triangle M^*}$ erhöhend bzgl. M so exist in $G_{M\triangle M^*}$ ein inklusionsmaximaler Weg, der Weg P in G induziert mit $w(P\cap M^*) > w(P \cap M)$

⇒ beide Endkanten von P gehören zu M oder eine Endkante gehört nicht zu M und ist inzident zu einem Knoten v, v nicht durch M gematcht. 

⇒ P erhöhend bzgl. M. (widerspruch)

#### Lemma

$G=(V,E), w:E\to \mathbb{R}, v \in V$, M Matching in $G-v$ (Graph induziert durch $V\setminus \{v\}$)

Dann gilt:

1. Falls es keinen bzgl. M erhöhenden Weg in G gibt mit Endknoten v, so hat M auch in G max. Gewicht
2. Falls es bzgl. M erhöhenden Weg in G gibt mit Endknoten v und $w(P\cap E\setminus M) - w(P\cap M)$ maximal unter allen solchen erhöhenden Wegen, so ist $M^* = M \triangle P$ Matching maximalen Gewichts in G.

`bild i) ii)`

#### Beweis

erhöhender Weg bzgl. M in G muss v als Endknoten haben. Sei $M^*$ max. Matching in G ⇒ $M\triangle M^*$ ist Menge von alternierenden Kreisen und Wegen bzgl. M bzw $M^*$ in G

P erhöhender Weg bzgl. M in $G_{M\triangle M^*}$ ⇒ P erhöhender Weg bzgl. M in G.

Da $G_{M\triangle M^*}$ höchstens bzgl. M erhöhender Weg $P^*$ mit Endknoten v enthält gilt $w(M)-w(P^*\cap M) = w(M^*) - w(P^*\cap M^*)$

Gewicht des Matching M', das durch erhöhen entlang $P^*$ entsteht ist: $$w(M') = w(M) - w(P^*\cap M) + w(P^*\cap E\setminus M) = w(M) - w(P^* \cap M) + w(P^*\cap M^*)$$
$$ \Rightarrow $$
$$ w(M') = w(M^*)$$

---

> 2015-05-20 14:10:24 

## Matching-Algorithmus für pl. Graph $G=(V,E)$

1. Zerlege G in $G_1, G_2$ durch Separator S entspr. Planar-Separator-Theorem und berechne rekursiv in $G_1$ und $G_2$ Matchings $M_1$ bzw. $M_2$ maximalen Gewichts; bezeichne $M=M_1 \cup M_2$
2. Solange $S\neq \emptyset$
	* wähle $v \in S, S:=S\setminus{\{v\}}$ und berechne mit Lemma aus $M'$ matching max. Gewichts in $G'+v$

---

$$t(n) = t(c_1 n) + t(c_2 n) + c_3 \cdot \sqrt{n} \cdot t'(n)$$

t'(n) Laufzeit für Lemma, $c_1,c_2,c_3$ Konstante; $c_1,c_2 \leq {2\over 3}, c_1+c_2 \leq 1$


Mit Master-Theorem kann t(n) abgeschätzt werden durch
$$t(n) \in O(n^{3\over 2}) \text{falls } t'(n) \in O(n)$$
$$t(n) \in O(n^{3\over 2} \log n) \text{falls } t'(n) \in O(n \log n)$$

## Mixed-Max-Cut in pl. Graphen

$G=(V,E), S\subseteq E$ _Schnitt_ von G falls durch $E\setminus S$ induz. Subgraph unzusammenhängend und für alle $\{u,v\} \in S$ u und v in verschiedenen Zusammenhangskomponenten dieses Subgraphs.


Kantengewichte $w:E\to \mathbb{R}$

#### Mixed-Max Cut

 Finde Schnitt S mit $w(s) = \sum_{l\in S} w(l)$ maximal.

Ist in bel. Graphen NP-schwer.

#### Beobachtung

\textsc{Mixed-Max Cut} Problem und \textsc{Mixed-Min Cut} Problem äquivalent.

Spezialfall: \textsc{Min Cut} Problem mit $w:E\to \mathbb{R}^{+}_0$ ist auch für bel. Graphen in P

polynomialer Algorithmus für \textsc{Mixed-Max Cut} in pl. Graphen:

verwende:

- Dualität von Schnitten und Kreisen
- max. Matching bzw. Planar Separator Theorem

Laufzeit in $O(n^{3/2} \log n)$.

Es gilt: G enthält Euler-Kreis g.d.w. E kantendisjunkte Vereinigung einfacher Kreise g.d.w. für alle $v\in V$ ist Knotengrad $d(w)$ gerade.

Dualität von Schnitt in G und Menge von einf. Kreisen (= Kantenmenge, in der f.a. Knoten v $d(v)$ gerade (= gerade Menge)) in Dualgraph $G^*$ (bzgl. bel. pl. Einbettung)

`bild gewichteter dualgraph`

\begin{itemize}
\item[Schritt 1]

trianguliere G in O(n); zusätzliche Kanten erhalten Gewicht 0

\item[Schritt 2]

berechne in O(n) Dualgraph bzgl. bel. pl. Einbettung; $G^*$ ist dann 3-regulär (d.h. für alle v: d(v) = 3)

\item[Schritt 3]

konstruiere zu $G^*$ Graph $G'$ so dass perfektes Matching min. Gewichts in G' eine gerade Menge (bzw. Menge von Kreisen) max. Gewichts in $G^*$ induziert.

\item[Schritt 4]

berechne in $O(n^{3/2} \log n)$ solch ein Matching bzw. gerade Menge

\item[Schritt 5]

falls diese gerade Menge nicht leer, gib entspr. Schnitt aus. Ansonsten "Sonderfall"

\end{itemize}

Matching M in $G=(V,E)$ mit $|V|$ gerade heißt perfekt falls $|M|=\frac{|V|}{2}$

---

#### zu Schritt 3

beachte dass $G^*$ 3-regulär, Matching ergibt zwei Fälle:

`Dreieck mit kante an jeder Ecke`

_Fall 1_: `Alle drei äußeren Kanten gematcht` Fall 2: `Eine kante von dreieck, eine äußere`
`bild `


$G'$ entsteht aus $G^*$ indem jeder Knoten durch Dreieick ersetzt wird. Sei m #Kanten in $G^*$, n #Knoten in $G^*$ ⇒ $3n = 2m$ ⇒ n gerade ⇒ #Knoten in G' gerade

#### zu Schritt 4

konstruiere perfektes Matching min. Gewichts in $G'$

__Beobachtung__: M perfektes Matching min. Gewichts in $G=(V,E)$ mit $w:E\to \mathbb{R}$ g.d.w. M perfektes Matching max. Gewichts bzgl. Gewichtsfkt. $\overline{w}:E\to \mathbb{R}$ mit $\overline{w}(l):=W-w(l)$, W geeignet gewählte Konstante.

_Erzwinge_ dass Matching max. Gewichts _perfekt_ ist:

- zu M perfekt betrachte $$\overline{w}(M) = \sum_{l\in M} \overline{w}(l) = \frac{n}{2} W - \sum_{l \in M} w(l) \geq \frac{n}{2} \cdot (W-w_{max})$$, wobei $w_{max} = \max_{l \in E} w(l)$
- zu M' nicht perfekt gilt $$\overline{w}(M') \leq (\frac{n}{2}-1)(W-w_{min}), w_{min} = \min_{l\in E} w(l)$$.

Wähle also W so dass $\frac{n}{2} \cdot (W-w_{max}) > (\frac{n}{2}-1)(W-w_{min})$

#### zu Schritt 5

Komplementmenge von perfekten Matching min. Gewichts in G' induziert gerade Menge max. Gewichts in $G^*$ und damit max. Schnitt in G.

Es kann sein, dass resultierende Menge leer ist! Passiert wenn max. Schnitt negatives Gewicht hat.


→ _Sonderfall_: Wollen nichttrivialen Schnitt erzwingen.

betrachte wieder Schritt 3: erzwinge, dass in perfekten Matching minimalen Gewichts für mindestens ein Knoten v aus $G^*$ Fall 2 eintritt.

_Vorgehensweise_: betrachte alle Knoten v aus $G^*$ und $G^* - v$ sowie durch perfektes Matching in G' induzierte Matching in $G^*-v$ und berechne mit "Matching-Lemma" Matching in $G^*$.  
Wähle M mit $w(M) = \min{v\in V^*} w(M_v)$

_Frage_: Wie kann man dabei Fall 2 an v erzwingen?
