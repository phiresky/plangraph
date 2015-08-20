> (Beginn Vorlesung 2015-06-16)

#### Satz von Okamura und Seymour

Falls Geradheitsbedingung erfüllt, so ist Kapazitätsbedingung hinreichend für Lösbarkeit

#### Lemma

Es gilt $fcap(X)$ gerade für alle $X\subseteq V$ g.d.w. $\equalto{fcap(v)}{\text{fcap}(\{v\}) = \underset{\text{Grad}}{d(v)} - \underset{\text{\#Terminale auf v}}{dens(v)}}$ gerade für alle $v\in V$.


#### Beweis

$\implies$ trivial

⇐: sei $fcap(v)$ gerade für alle $v\in V$. Betrachte $X\subseteq V$:
$$cap(X) = \sum_{v\in X} cap(v) - 2\cdot |\{\{u,v\}\in E: u,v\in X\}|$$
$$dens(X) = \sum_{v\in X} dens(v) - 2 \cdot |\{\{s_i,t_i\}\in D: s_i,t_i \in X\}|$$
$$fcap(X) = \sum_{v\in X} cap(v) - \sum_{v\in X} dens(v) - 2\cdot |\{\{u,v\} \in E: u,v \in X\}| + 2\cdot |\{\{s_i,t_i\} \in D: s_i, t_i \in X\}|$$

-> fcap(X) gerade

Geradheitsbedingung überpfrüfen: Es reicht für alle $v\in V$ den Grad von v und \# $s_i,t_i$ auf V zu zählen.

Linearzeitalgorithmus für $G=(V,E)$ pl., Terminalpaare D auf äußerer Facette und Geradheitsbedingung erfüllt.

### 2 Phasen

1. Konstruiere aus G,D "einfache Instanz" mit "Klammerstruktur" und berechne mittels RIGHT-FIRST Tiefensuche Lösungswege $q_1,\dots,q_k$. Diese induzieren gerichteten "Hilfsgraph".
2. Berechne mittels gerichteter RIGHT-FIRST Tiefensuche in Hilfsgraph Lösungswege $p_1 \dots p_k$ die jeweils $s_i$ mit $t_i$ verbinden.

### Instanz mit Klammerstruktur

$G,D = \{\{s_i,t_i\}:s_i,t_i\in V\} s_i,t_i$ alle auf äußerer Facette

*(todo: bild bild)*

daraus Instanz mit Klammerstruktur konstruieren:

- wähle beliebiges Terminal als "Startterminal" s
- gehe im Gegenuhrzeigersinn startend von s um äußere Facette und ordne erste Terminal aus einem Paar $\{s_i,t_i\}$ eine "(" zu und zweitem Auftreten eine ")"

$\leadsto$ Klammerausdruck; paare Terminal entsprechend Klammerausdruck

$\leadsto$ Instanz $G=(V,E), D'=\{\{s_i',t_i'\}:s_i',t_i'\in V\}$ entsprechende Klammerung

Konstruiere mittels RF-Suche Lösung $q_1\dots q_k$ zu $G,D'$; Reihenfolge in der Wege bezeichnet werden nach Reihenfolge der $t_i'$, d.h. "von innen nach außen" in Klammerstruktur

### Korrektheit von Phase 1

#### Beobachtung

i) keine zwei Wege $g_i,g_j$ kreuzen sich und 
ii) kein $g_i$ kreuzt sich selbst (wegen RF-Auswahlregel)

Sei $\vec{G}=(V,\vec{E})$ Graph der durch $q_1\dots q_k$ induziert wird. Dann enthält $\vec G$ keinen Rechtskreis.
*(todo: bild)*
=> induktiv über $q_i, 1\leq i \leq k$ kann gezeigt werden, dass $q_i'$ die "richtigen Terminale" verbindet.

1. Phase in $O(n)$ klar. in 
