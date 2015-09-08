# s-t-Flüsse

> (Beginn Vorlesung 2015-05-26)

Siehe Folien ([slides/flow_slides.pdf](slides/flow_slides.pdf))

## Beweis zu Folie "Kozykel und st-Schnitte"

1) s,t auf selber Seite von $C^*$ ⇒ P kreuzt $C^*$ gleich oft in jeder Richtung ⇒ C enthält selbe Zahl von Kanten in P und rev(P) ⇒ $\pi(C) = 0$
2) s rechts, t links ⇒ P kreuzt einmal mehr von rechts nach links ⇒ $\pi(C) = 1$
3) analog ⇒ $pi(C) = -1$

C $s,t$-Schnitt ⇒ P kreuzt $C^*$ von rechts nach links ⇒ $\pi(C) = 1$.
$\pi(C) = 1$ ⇒ Fall 2; s rechts, t links. ⇒ C st-Schnitt.

## Beweis zu Folie "Betrachte Fluss von $\lambda$ auf P"

#### Beweis:

"⇒" Angenommen $G^*_λ$ enthält neg. Kreis $C^*$
$$0 > c(λ, C^*) = \sum_{e\in C} c(λ,e) = \sum_{e\in C} c(e) - λ\sum_{e\in C} \pi(e) = \underbrace{\sum_{e\in C}c(e)}_{\geq 0} - \underbrace{λ}_{\geq 0} \underbrace{\pi(C)}_{> 0}$$
$$ \implies \pi(C) = 1. \implies \text{C ist st-Schnitt}$$

Außerdem $\sum_{e\in C} c(e) < λ \implies$ st-Schnitt mit Kap. < $λ$.

"⇐": $G^*_λ$ enthält keinen neg. Kreis ⇒ kürzeste Wege wohldef.

Wähle o in $G^*_λ$ bel. Ursprung.

$dist(λ,p)$: Distanz von p zu o in $G^*_λ$.

Def: $\phi(λ,e) := dist(λ, head(e^*)) - dist(λ,tail(e^*)) + λ\cdot\pi(e)$

Zeige: $\phi$ ist gültiger st-Fluss.

1)  Für $v\in V$ gilt: $\sum_{W} \phi(v \to w) = \sum_W \pi(v \to w)$

    $\implies \phi(λ, \cdot)$ ist Fluss mit Wert $λ$.
2) $slack(λ,e^*) := dist(λ,tail(e^*)) + c(λ,e) - dist(λ,head(e^*))$

    Gilt: $slack(λ,e) = c(e) - \phi(λ,e)$

	$\phi(λ,e) \leq c(e) \Leftrightarrow slack(λ,e) \geq 0.$ 

	Wäre $slack(λ,e) < 0 \implies dist(λ,head(e^*)) > dist(λ,tail(e^*)) + c(λ,e^*))$ (widerspruch)

Max $λ$ sodass kein neg. Kreis in $G^*_λ$ ist Länge eines kürzesten ts-Wege in $G^*_λ$.
