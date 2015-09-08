## Matching-Algorithmus für planare Graph $G=(V,E)$

> (Beginn Vorlesung 2015-05-20)

1. Zerlege G in $G_1, G_2$ durch Separator S entspr. Planar-Separator-Theorem und berechne rekursiv in $G_1$ und $G_2$ Matchings $M_1$ bzw. $M_2$ maximalen Gewichts; bezeichne $M=M_1 \cup M_2$
2. Solange $S\neq \emptyset$
	* wähle $v \in S, S:=S\setminus{\{v\}}$ und berechne mit Lemma aus $M'$ matching max. Gewichts in $G'+v$

---

$$t(n) = t(c_1 n) + t(c_2 n) + c_3 \cdot \sqrt{n} \cdot t'(n)$$

t'(n) Laufzeit für Lemma, $c_1,c_2,c_3$ Konstante; $c_1,c_2 \leq {2\over 3}, c_1+c_2 \leq 1$


Mit Master-Theorem kann t(n) abgeschätzt werden durch
$$t(n) \in O(n^{3\over 2}) \text{falls } t'(n) \in O(n)$$
$$t(n) \in O(n^{3\over 2} \log n) \text{falls } t'(n) \in O(n \log n)$$

# Mixed-Max-Cut in planaren Graphen

$G=(V,E), S\subseteq E$ _Schnitt_ von G falls durch $E\setminus S$ induz. Subgraph unzusammenhängend und für alle $\{u,v\} \in S$ u und v in verschiedenen Zusammenhangskomponenten dieses Subgraphs.


Kantengewichte $w:E\to \mathbb{R}$

#### Mixed-Max Cut

 Finde Schnitt S mit $w(s) = \sum_{l\in S} w(l)$ maximal.

Ist in bel. Graphen NP-schwer.

#### Beobachtung

\textsc{Mixed-Max Cut} Problem und \textsc{Mixed-Min Cut} Problem äquivalent.

Spezialfall: \textsc{Min Cut} Problem mit $w:E\to \mathbb{R}^{+}_0$ ist auch für bel. Graphen in P

polynomialer Algorithmus für \textsc{Mixed-Max Cut} in planaren Graphen:

verwende:

- Dualität von Schnitten und Kreisen
- max. Matching bzw. Planar Separator Theorem

Laufzeit in $O(n^{3/2} \log n)$.

Es gilt: G enthält Euler-Kreis g.d.w. E kantendisjunkte Vereinigung einfacher Kreise g.d.w. für alle $v\in V$ ist Knotengrad $d(w)$ gerade.

Dualität von Schnitt in G und Menge von einf. Kreisen (= Kantenmenge, in der f.a. Knoten v $d(v)$ gerade (= gerade Menge)) in Dualgraph $G^*$ (bzgl. beliebiger planarer Einbettung)

*(todo: bild gewichteter dualgraph)*

Schritt 1
  ~ trianguliere G in O(n); zusätzliche Kanten erhalten Gewicht 0

Schritt 2
  ~ berechne in O(n) Dualgraph bzgl. beliebiger planarer Einbettung; $G^*$ ist dann 3-regulär (d.h. für alle v: d(v) = 3)

Schritt 3
  ~ konstruiere zu $G^*$ Graph $G'$ so dass perfektes Matching min. Gewichts in G' eine gerade Menge (bzw. Menge von Kreisen) max. Gewichts in $G^*$ induziert.

Schritt 4
  ~ berechne in $O(n^{3/2} \log n)$ solch ein Matching bzw. gerade Menge

Schritt 5
  ~ falls diese gerade Menge nicht leer, gib entspr. Schnitt aus. Ansonsten "Sonderfall"

Matching M in $G=(V,E)$ mit $|V|$ gerade heißt perfekt falls $|M|=\frac{|V|}{2}$

---

#### zu Schritt 3

beachte dass $G^*$ 3-regulär, Matching ergibt zwei Fälle:

*(todo: Dreieck mit kante an jeder Ecke)*

_Fall 1_: *(todo: Alle drei äußeren Kanten gematcht)* Fall 2: *(todo: Eine kante von dreieck, eine äußere)*
*(todo: bild )*


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

