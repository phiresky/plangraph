# Das Menger-Problem

Zur Erinnerung: $S \subset V$ heißt _Separator_ in $G=(V,E)$, falls $G-S$ unzusammenhängend. $S \subset E$ heißt _Schnitt_ in $G=(V,E)$ falls der durch $E\setminus S$ induzierte Teilgraph von G unzusammenhängend.

Zu $u,v \in V$ def:
$$K_G(u,v) := \begin{cases} |V|-1 \text{ falls } \{u,v\} \in E \\ min_{S \subset V} |S| \text { sonst} \end{cases}$$

und $$K(G) := \min_{u,v\in V} K_G(u,v) = \min_{\text{S Separator in G}} \{|S|, |V|-1\}$$

$$λ_G(u,v) := \min_{S \subset E} |S|$$

$$λ(G) := \min_{u,v\in V} λ_G(u,v) = \min_{S \subset E, \text{S Schnitt in G}} |S|$$

Zwei Wege heißen _kantendisjunkt_, wenn sie keine gemeinsame Kante enthalten und (intern) _knotendisjunkt_ wenn sie (außer Anfangs- und Endknoten) keinen Knoten gemeinsam haben.

## Satz von Menger

Seien s und t Knoten in $G=(V,E)$ ($\{s,t\} \notin E$ bei knotendisj. Version)

- $\Kappa_G(s,t) \geq k$ g.d.w. es mind. k paarweise knotendisj. s-t-Wege gibt
- $λ_G(s,t) \geq k$ g.d.w. es mind. k paarweise kantendisj. s-t-Wege gibt

## Menger-Problem

Zu $G=(V,E)$, $s,t \in V$ finde max. Anzahl knotendisj. bzw. kantendisj. s-t-Wege.

### Menger-Problem in pl. Graphen; kantendisj. Variante

#### Linearzeitalgorithmus basierend _Right-First-DFS_

_Spezialfall_: s und t liegen auf derselben Facette

*(todo: Bild)*

RIGHT-FIRST $\hat=$ im Gegenuhrzeigersinn nächste freie Kante in Adjazenzliste (relativ zur aktuellen eingehenden Kante)

---

Linearzeitalgorithmus bestehend aus 4 Schnitten; $G=(V,E)$ planar eingebettet, o.B.d.A. t auf äußerer Facette.

#### 1. Schritt

ersetze $G=(V,E)$ durch $\vec{G} = (V,\vec{E})$ indem $\{u,v\} \in E$ durch $(u,v)$ und $(v,u)$ ersetzt wird. (In $O(n)$)

#### 2. Schritt

berechne in $O(n)$ Menge gerichteter einfacher kantendisj. Kreise $\vec{C}_1,\dots,\vec{C_l}$ und konstruiere (in $O(n)$) aus $\vec{G}$ Graph $\vec{G_C} = (V, \vec{E_C})$, der entsteht in dem alle Knoten auf den $\vec{C}_i$ umgedreht werden.

#### 3. Schritt

berechne in $\vec{G}_C$ in $O(n)$ mittels RIGHT-FIRST-DFS eine max. Anzahl kantendisj. gerichteter s-t-Wege.

#### 4. Schritt

berechne aus dem in Schritt 3 gefundenen s-t-Wegen in $\vec{G}_C$ gleiche Anzahl kantendisj. s-t-Wege in G in $O(n)$.

---

### zu Schritt 1

*(todo: Bild)*

**Lemma**: Seien $p_1,\dots,p_r$ kantendisjunkte gerichtete s-t-Wege in $\vec{G}$. Dann enthält $P=\{\{u,v\}\in E:$ genau eine der Kanten (u,v) und (v,u) liegt auf einem der $p_i\}$ gerade r kantendisjunkte s-t-Wege in G.

**Beweis**: zwei Fälle
*(todo: Bilder)*

### Zu Schritt 2

$C_1,\dots,C_l$ in $\vec{G}$ so dass
1. $\vec{G}_C$ enthält keine Rechtskreise, d.h. keine Kreise deren Inneres rechts liegt.
2. Sei $\vec{P}_C \subseteq \vec{E}_C$ Menge der Kanten auf kantendisjunkten s-t-Wegen in $\vec{G}_C$ und $\vec{P} \subseteq \vec{E}$ wobei $$\vec{P}:=(\vec{P}_C \cap \vec{E}) \cup \{(u,v) \in \vec{E}: (u,v) \text{ auf einem der }\vec{C}_i \text{ und } (v,u)' \notin \vec{P}_C\}$$

Dann induziert $\vec{P}$ k kantendisjunkte gerichtete s-t-Wege in $\vec{G}$ g.d.w. $\vec{P}_C$ k kantendisjunkte gerichtete s-t-Wege in $\vec{G}_C$ induziert.

### Konstruktion der Kreise $C_1\dots C_l$

sei f Facette in G bzw. $\vec{G}$; def. Abstand von f von äußerer Facette als

 $dist(f):=$ Länge eines kürzesten Weges von Dualknoten zu f zu Dualknoten zu äußerer Facette $f_0$ in $G^*$

def. $C_i$ als Vereinigung der einfachen Kreise in G für die alle Facetten f im Inneren $dist(f)\geq i$ erfüllen. $\vec{C}_i$ sei entsprechend Rechtskreis in $\vec{G}$.

Drehe alle diese $\vec{C}_i$ um -> $\vec{G}_C$
