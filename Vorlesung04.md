# Separatoren in planaren Graphen

> (Beginn Vorlesung 2015-05-05)

(siehe [planarseparator_slides.pdf](planarseparator_slides.pdf))

PST: pl. $G=(V,E);$ existiert Separator S der G in $G_1=(V_1,E_1), G_2=(V_2,E_2)$ trennt mit

1. $|V_1|,|V_2| \leq {2 \over 3} n$
2. $|s| \leq 4 \sqrt{n}$

## Bemerkung zu Planar Separator Theorem: Linearzeitimplementierung

Separator S kann in Linearzeit gefunden werden.
Kritische Stelle im Beweis des wichtigen Lemmas: Kreis induziert durch Nichtbaumkante

## Fall 2 im Beweis des Lemmas

* Vergleich $|Inneres K_{xt}|$ mit $|Inneres K_{ty}|$
* amortisierte Analyse: Zuordnung der Iteration zu dem Kreis, der nicht mehr betrachtet wird

# Matching in planaren Graphen

> (Beginn Vorlesung 2015-05-12)

$G=(V,E)$, ein Matching $M \subseteq E$ sodass keine zwei Kanten aus M gemeinsame Endknoten haben.

$w:E\to\mathbb{R}$

- Finde $M \subseteq E$ _Matching mit max. Gewicht_, wobei $w(m)=\sum_{l \in M} w(l)$
- Finde $M \subseteq E$ _Matching mit max. Kardinalität_, (Fall $w(l) = 1$ f.a. $l \in E$)

Beide Probleme sind auch für bel. Graphen in P.

*(todo: bild)*

alternierender Weg bzgl. M → Vertauschen der Kanten auf Weg aus M mit Kanten auf Weg, die nicht in M sind resultiert in größerem Matching M*

---

- Ein bezüglich einem Matching M _alternierender Weg_ ist ein einfacher Weg oder einfach Kreis, dessen Kanten abwechselnd in M und $E\setminus M$ sind.
- Alternierender Weg P (bezeichne entsprechende Kantenmenge) ist _erhöhender Weg_ falls $$\sum_{l \in P, l \in E \setminus M} w(l) > \sum_{l \in P, l \in M} w(l)$$ und P entweder Kreis (gerader Länge) oder dessen erste und letzte Kante beide in M sind oder inzident zu einem ungematchten Knoten.

#### Beobachtung

M Matching, P erhöhender Weg bzgl M ⇒ $M'=(M\setminus P) \cup (P\setminus M)$ wieder Matching mit $w(M')>w(M).$

#### Lemma

Sei $G=(V,E), w:E\to \mathbb{R}$, M Matching in G. Dann ist $w(M)$ maximal genau dann wenn es keinen erhöhenden Weg bzgl. M gibt.

#### Beweis

"⇒" klar

"⇐" sei M nicht max. Matching in G und es existiert kein bzgl. M erhöhender Weg. Dann exististiert Matching $M^*$ mit $w(M^*) > w(m)$. Betrachte Subgraph $G_{M^*\triangle M}$ von G der durch $$M^*\triangle M = M \cup M^* \setminus(M\cap M^*)$$ induziert wird. In diesem Graph haben alle Knoten Grad 1 und Grad 2 und er besteht aus einfachen Wegen und Kreisen.  
Falls kein Kreis in $G_{M\triangle M^*}$ erhöhend bzgl. M so existiert in $G_{M\triangle M^*}$ ein inklusionsmaximaler Weg, der Weg P in G induziert mit $w(P\cap M^*) > w(P \cap M)$

⇒ beide Endkanten von P gehören zu M oder eine Endkante gehört nicht zu M und ist inzident zu einem Knoten v, v nicht durch M gematcht. 

⇒ P erhöhend bzgl. M. (widerspruch)

#### Lemma

$G=(V,E), w:E\to \mathbb{R}, v \in V$, M Matching in $G-v$ (Graph induziert durch $V\setminus \{v\}$)

Dann gilt:

1. Falls es keinen bzgl. M erhöhenden Weg in G gibt mit Endknoten v, so hat M auch in G max. Gewicht
2. Falls es bzgl. M erhöhenden Weg in G gibt mit Endknoten v und $w(P\cap E\setminus M) - w(P\cap M)$ maximal unter allen solchen erhöhenden Wegen, so ist $M^* = M \triangle P$ Matching maximalen Gewichts in G.

*(todo: bild i) ii))*

#### Beweis

erhöhender Weg bzgl. M in G muss v als Endknoten haben. Sei $M^*$ max. Matching in G ⇒ $M\triangle M^*$ ist Menge von alternierenden Kreisen und Wegen bzgl. M bzw $M^*$ in G

P erhöhender Weg bzgl. M in $G_{M\triangle M^*}$ ⇒ P erhöhender Weg bzgl. M in G.

Da $G_{M\triangle M^*}$ höchstens bzgl. M erhöhender Weg $P^*$ mit Endknoten v enthält gilt $w(M)-w(P^*\cap M) = w(M^*) - w(P^*\cap M^*)$

Gewicht des Matching M', das durch erhöhen entlang $P^*$ entsteht ist: $$w(M') = w(M) - w(P^*\cap M) + w(P^*\cap E\setminus M) = w(M) - w(P^* \cap M) + w(P^*\cap M^*)$$
$$ \Rightarrow $$
$$ w(M') = w(M^*)$$

---
