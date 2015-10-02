import java.util.*;

class Trees{
	public static void main(String[] args){
		Person ormond = new Person("ormond", null);
		Person steffon = new Person("steffon", ormond);
		Person robert = new Person("robert", steffon);
		Person joffrey = new Person("joffrey", robert);
		Person myrcella = new Person("myrcella", robert);
		Person tommen = new Person("tommen", robert);
		Person stannis = new Person("stannis", steffon);
		Person shireen = new Person("shireen", stannis);
		Person renly = new Person("renly", steffon);

		System.out.println(renly.isParentOf(stannis) + "\n");
		System.out.println(steffon.isParentOf(renly) + "\n");
		System.out.println(ormond.isAncestorOf(renly) + "\n"); 
		System.out.println(robert.isAncestorOf(joffrey) + "\n");
		System.out.println(stannis.isAncestorOf(myrcella) + "\n");
		ormond.getAllDescendantsDepthFirst().forEach(p -> System.out.println(p.name));

		System.out.println();
		ormond.getAllDescendantsBreadthFirst().forEach(p -> System.out.println(p.name));
		System.out.println();
		steffon.getAllDescendantsBreadthFirst().forEach(p -> System.out.println(p.name));
	}

	static class Person{
		String name;
		ArrayList<Person> children;
		Person parent;

		public Person(String name, Person parent){
			this.name = name;
			this.children = new ArrayList<Person>();
			this.parent = parent;
			if(parent != null){
				parent.children.add(this);
			}
		}

		@Override public boolean equals(Object other){
			return other instanceof Person && this.name.equals(((Person)other).name);
		}

		public boolean isParentOf(Person other){
			return children.contains(other);
		}

		public boolean isAncestorOf(Person other){
			if(this.isParentOf(other)) return true;
			if(this.children.size() == 0) return false;
			for(Person child : children){
				if(child.isAncestorOf(other)) return true;
			}
			return false;
		}

		public ArrayList<Person> getAllDescendantsDepthFirst(){
			ArrayList<Person> descendants = new ArrayList<Person>();
			descendants.add(this);
			for(Person child : children){
				descendants.addAll(child.getAllDescendantsDepthFirst());
			}
			return descendants;
		}

		public ArrayList<Person> getAllDescendantsBreadthFirst(){
			ArrayList<Person> descendants = new ArrayList<>();
			descendants.add(this);
			descendants.addAll(getAllDescendantsBreadthFirstExclusive());
			return descendants;
		}

		public ArrayList<Person> getAllDescendantsBreadthFirstExclusive(){
			ArrayList<Person> descendants = new ArrayList<>();
			//descendants.add(this);
			for(Person child : children){
				descendants.add(child);
			}
			for(Person child : children){
				descendants.addAll(child.getAllDescendantsBreadthFirstExclusive());
			}
			return descendants;
		}
	}
}

