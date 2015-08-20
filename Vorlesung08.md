> (Beginn Vorlesung 2015-06-03)

### Zu Schritt 2 (Wdh)

$C_1,\dots,C_l$ geeignete Kreise in G; $\vec{C}_1,\dots,\vec{C}_l$ entsprechende Rechtskreise in $\vec{G}$ drehe $\vec{C}_1,\dots,\vec{C}_l$ um ~> $\vec{G}_C$; $\vec{G}_C$ enthält keine Rechtskreise, da für jeden Rechtskreis in $\vec{G}$ beim Übergang zu $\vec{G}_C$ mindestens eine Kante des Kreises umgedreht wird.

Sei $\vec{P}_C \subset \vec{E}_C$ Kantenmenge zu k s-t-Wegen in $\vec{G}_C$. Konstruiere dazu Kantenmenge $\vec{P}$ in $\vec{G}$

$$ \vec{P} := \text{siehe oben}$$

`Bild`


### Zu Schritt 3

Berechnung einer max. Anzahl s-t-Wege in $G_C$ in $O(n)$

- Schleife über ausgehende Kanten aus s
    - RIGHT-FIRST-DFS-Tiefensuche
    - Suchschritt: rechteste freie auslaufende Kante in Bezug auf Referenzkante
	    
		2 Varianten welche "Referenzkante"

		- **Weihe**: aktuell einlaufende Kante
		- **Coupry**: erste einlaufende Kante

#### Korrektheitsbeweis zu Schritt 3

Zu beweisen: $\vec{P}_C$ enthält maximale Anzahl s-t-Wege. Benutze dazu gewichtete Variante des Satz von Menger, d.h. konstruiere s-t-Schnitt, der entsprechende Kapazität hat.

Schnitt A wird induziert durch geeigneten Kreis $\vec{K}$ in $\vec{G}_C$ mit folgenden Eigenschaften:

i) $s\in \text{Inneres}(\vec{K})$ oder auf $\vec{K}$
ii) $t\in \text{Äußeres}(\vec{K})$
iii) $|A:=\{(u,v)\in \vec{E}_C: u \text{ auf }\vec{K}, v\in \text{Äußeres}(\vec{K})\}|$ ist gleich #s-t-Wege in $\vec{P}_C$

$\vec{K}$ wird mittels LEFT-FIRST Rückwärtssuche von s aus in $\vec{P}_C$ konstruiert

`Bild: Kreis mit t ausserhalb: Varianten wie K aussieht: 1. S liegt auf Kreis, 2. S liegt in Kreis`

#### Lemma

Betrachte $\vec{G}_C = (V,\vec{E}_C)$ und $\vec{K}$, dann ist jede Kante $(u,v) \in \vec{E}_C$ mit M auf $\vec{K}$ und $v\in \text{Äußeres}(\vec{K})$ durch einen s-t-Wege aus $\vec{P}_C$ besetzt


#### Beweis

i) wenn $p_1,\dots,p_l$ s-t-Wege und linkskreise von s nach s. Dann gehört keine der Kanten $(X,Y), X \in \text{Äußeres}(\vec{K})$ und y auf $\vec{K}$ zu einem der $p_i$ `bild`

    wegen Left-First in Graph induziert durch $p_1,\dots,p_l$ $(u,y)\notin p_i$ für alle $1 \leq i \leq l$ ⇒ für $(u,v)$ mit u auf $\vec{K}, r\in \text{Äußeres}(\vec{K})$ kann nicht auf einem Linkskreis aus $p_1,\dots,p_l$ liegen.

 ii) betrachte $(u,v)$ mit u auf $\vec{K}, v \in \text{Äußeres}(\vec{K})$ und $(u,w)$ mit w auf $\vec{K}$ `bild`

     _Annahme_: $(u,v)$ gehört zu keinem der $p_1,\dots,p_l$

	 betrachte Referenzkante zu (u,w) in RIGHT-FIRST-SUCHE (Schritt 3)

	 Referenzkante "liegt wie" `grün` oder `blau`, aber dann hätte RIGHT-FIRST _nicht_ (u,w) sondern (u,v) ⇒ Widerspruch
