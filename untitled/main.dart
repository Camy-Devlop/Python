void main() {
  Bonbon l = new Bonbon(durter: "oui", title: "tagada",couleur: "rose");
  l.affiche();
}

class Bonbon {
  String? durter;
  String? couleur;
  String? title;
  Bonbon({durter: "", couleur: "", String title = ""}) {
    this.durter = durter.toString();
    this.couleur = couleur.toString();
    this.title = title.toString();
  }

  void affiche() {
    print(this.title! + " la durter " + this.durter! + " " + this.couleur!);
  }
}
