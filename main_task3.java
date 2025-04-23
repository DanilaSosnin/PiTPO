import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

class tuple3<A, B, C> {
    public final A first;
    public final B second;
    public final C third;

    public tuple3(A first, B second, C third) {
        this.first = first;
        this.second = second;
        this.third = third;
    }

    public String toString() {
        return "(" + first + ", " + second + ", " + third + ")";
    }
}

public class Main {
    public List<String> fragments;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int Blocks = sc.nextInt();
        List<String> fragments = new ArrayList<>();
        List<String> fragments_cutted = new ArrayList<>();
        List<Integer> busyindexes = new ArrayList<>();
        System.out.println(" ");
        sc.nextLine();

        for (int i = 0; i < Blocks; i++) {
            while (true) {

                String fragment = sc.nextLine();

                if (fragment.isEmpty()) {
                    break;
                }
                fragments.add(fragment);
            }

            fragments.sort(Comparator.comparingInt(String::length));
            fragments_cutted = new ArrayList<>(fragments);
            int fileLength = fragments.get(0).length() + fragments.get(fragments.size() - 1).length();
            tuple3<String, Integer, Integer> candidate = new tuple3<>(fragments.get(0) + fragments.get(fragments.size()-1), 0, fragments.size()-1);
            fragments_cutted.remove(0);
            fragments_cutted.remove(fragments_cutted.size()-1);
            if (fragments.size() % 2 == 0) {
                System.out.println(fragmentsJoiner(fragments, fragments_cutted, 0, fileLength, candidate));
            }
            else System.out.println("Указано нечётное количество элементов");
        }
    }

    public static String fragmentsJoiner(List<String> fragments, List<String> fragments_cutted, int i1, int length, tuple3<String, Integer, Integer> candidate) {

        for (int i = fragments_cutted.size() - 1; i > 0; i--) {

            if (fragments_cutted.get(i1).length() + fragments_cutted.get(i).length() == length &&
                    ((fragments_cutted.get(i1) + fragments_cutted.get(i)).equals(candidate.first) ||
                            (fragments_cutted.get(i) + fragments_cutted.get(i1)).equals(candidate.first))) {
                fragments_cutted.remove(i);
                fragments_cutted.remove(i1);
                if (fragments_cutted.size() > 1) return fragmentsJoiner(fragments, fragments_cutted, 0, length, candidate);
                else return candidate.first;
            }

            if (fragments_cutted.get(i1).length() + fragments_cutted.get(i).length() < length) {
                fragments_cutted = new ArrayList<>(fragments);
                tuple3<String, Integer, Integer> nc = chooseCandidate(candidate, fragments);
                if (nc.second > fragments.size() - 1) return "Комбинация не найдена.";
                int c1 = Math.max(nc.second, nc.third);
                int c2 = Math.min(nc.second, nc.third);
                fragments_cutted.remove(c1);
                fragments_cutted.remove(c2);
                return fragmentsJoiner(fragments, fragments_cutted, 0, length, nc);
            }
        }
        fragments_cutted = fragments;
        tuple3<String, Integer, Integer> nc = chooseCandidate(candidate, fragments);
        int c1 = nc.second;
        int c2 = nc.third;
        fragments_cutted.remove(c1);
        fragments_cutted.remove(c2);
        return fragmentsJoiner(fragments, fragments_cutted, 0, length, nc);
    }

    public static tuple3<String, Integer, Integer> chooseCandidate(tuple3<String, Integer, Integer> candidate, List<String>fragments) {
        int c1 = candidate.second;
        int c2 = candidate.third;
        String newCandidate = candidate.first;
        c2--;
        if (c2 == c1) c2--;

        if (c2 < 0 || (fragments.get(c1) + fragments.get(c2)).length() < candidate.first.length()) {
            c2 = fragments.size() - 1;
            c1++;
            if (c1 <= fragments.size() - 1) {
                while (c2 >= 0 && ((fragments.get(c1) + fragments.get(c2)).length() > candidate.first.length() || c1 == c2)) {
                    c2--;
                }
            }
            else {
                return new tuple3<>(newCandidate, c1, c2);
            }
        }

        if ((fragments.get(c1) + fragments.get(c2)).length() == candidate.first.length() &&
                !(fragments.get(c1) + fragments.get(c2)).equals(candidate.first)) {
            newCandidate = fragments.get(c1) + fragments.get(c2);
        }
        return new tuple3<>(newCandidate, c1, c2);
    }
}

/*
011
0111
01110
111
0111
10111
*/
