## Das knotendisjunkte Menger-Problem

geg. $G=(V,E), s,t\in V$. Finde eine maximale Anzahl paarweise (intern) knotendisj. s-t-Wege in G.

#### Satz von Menger

maximale Anzahl knotendisj. s-t-Wege ist gleich der Größe eines minimalen Separators, der s und t trennt.

Linearzeitalgorithmus für knotendisjunktes Menger-Problem in planaren Graphen basiert auf RIGHT-FIRST-Suche.

#### Schritt 1

überführe $G=(V,E)$ in gerichteten Graph $\vec{G}=(V,\vec{E}$ indem alle Kanten mit $u,v \in V\setminus \{s,t\}$ durch zwei gerichtete Kanten ersetzt werden. Kanten $\{s,v\}$ werden nur durch $(s,v)$ und $\{v,t\}$ nur durch $(v,t)$ ersetzt.

#### Schritt 2

Seien $l_1,\dots,l_r \in E$ die aus s auslaufenden Kanten, führe Schleife über $l_1,\dots,l_r$ aus, wobei im i-ten Durchlauf RIGHT-FIRSTT-Suche startend bei bei s mit $l_i$ ausgeführt wird. Durchlauf endet in t oder in s.

RIGHT-FIRST-Suche kann zu "Konflikt" führen, d.h. Suche trifft auf einen bereits belegten Knoten

- belegter Knoten:  `bild`

zwei mögliche Konfliktsituationen:

- Konflikt von links,
- Konflikt von rechts

1)   Konflikt von links (mit anderem Pfad oder selben Pfad früher)

     ⇒ BACKTRACK-REMOVE: ein Schritt zurück
2)  Konflikt von rechts
	a) zwischen zwei Wegen, gefundener Weg und Suchweg: Vorangehende Wegabschnitte von gefundenem Weg und Suchweg werden vertauscht ⇒ Konflikt von links
	b) Suchweg trifft von rechts auf sich selbst

		Trick: verhindere, dass ein Rechtskreis durchlaufen wird, indem nach vorherigen Durchlauf des entsprechenden Linkskreis geeignete Kante gelöscht wird.

		Man kann beweisen, dass für Kante $(v,w)$ die zu Rechtskreis mit Konflikt rechts in v führt zuvor umgekehrte Kante $(w,v)$ in einem Linkskreis mit Konflikt von links in v durchlaufen wird.

		$\leadsto$ lösche Kante $(v,w)$ die nach RIGHT-FIRST-Auswahlregel nächste Kante wäre (*) nachdem $(w,v)$ zuvor von denselben Suchweg belegt wurde.

		zweiter Trick: führe globalen Zähler ein, der um 1 erhöht wird, wenn neue Suche in s startet oder Wege umorganisiert werden wegen "Konflikt von rechts" setze Wert des "lokalen" Zählers um besuchten Knoten v auf Wert des globalen Zählers $\leadsto$ Situation (*) wird erkannt, da Wert des lokalen Zählers an v und w gleich.

#### Laufzeit

$O(n)$ klar, da jede Kante höchstens einmal besucht wird und RIGHT-FIRST-Auswahlschritt in $O(1)$; Referenzkante zu Knoten v bleibt gleich.

#### Korrektheit

wichtigster Teil ist Beweis, dass "gelöschte" Kante wegen "Backtrack-Remove" oder wegen (*) für Lösung nicht benötigt wird.

Sei k maximale Anzahl s-t-Wege in G und $a_1,\dots,a_n$ gelöschte Kanten (in dieser Reihenfolge).

Beweise per Induktion über $a_1 \dots a_n$ dass $G_i:=G\setminus \{a_1,\dots,a_n\}$ ebenfalls k s-t-Wege enthält.

# Das Problem von Okamura und Seymour

## Kantendisjunktes Wegpackungsproblem

Gegeben $G=(V,E)$ und Paare ausgezeichneter Knoten $\{s_1,t_1\},\dots,\{s_k,t_k\},s_i,t_i\in V$

Finde paarweise kantendisjunkte $s_i-t_i-$Wege.

NP-vollständig, sogar wenn G planar. Mögliche Spezialfälle: 

- G planar und $s_i,t_i$ für alle $1\leq i \leq k$ auf dem Rand derselben Facette
- G planar und sogar $G:=(V,E \cup D)$ wobei $D:=\{\{s_i,t_i\}: s_i,t_i \text{Terminale}\}$ planar

D für "Demand-Kanten"

$G=(V,E), D=\{\{s_i,t_i\}: 1\leq i \leq k, s_i, t_i \in V\}, X\subseteq V$. Dann heißt $$cap(X):=|\{\{u,v\}\in E, u\in X, v\in V\setminus X\}|$$ **Kapazität** von X (bzw. Kantenschnitt induziert durch X).

und $$ dens(X):=|\{\{s_i,t_i\}\in D: |\{s_i,t_i\}\cap X|=1\}|$$ **Dichte** von X.

$fcap(X):=cap(X)-dens(X)$ **freie Kapazität** von X.

Offensichtlich $fcap(X)\geq 0$ für alle $X \subset V$ notwendige Bedingung für Lösbarkeit.

`Bild` Also $fcap(X)\geq 0$ für alle Schnitte $X\subseteq V$ ist nicht hinreichend für Lösbarkeit!a

Weitere Bedingung an Instanz: Für alle $X\subseteq V$ fcup(X) gerade. __Geradheitsbedingung__
