public class LetterNode
{
    public LetterNode[] Alphabet { get; } = new LetterNode[26]; // Initialize to null
    public bool IsEnd { get; set; }
}

public class WordDictionary
{
    private LetterNode root;

    public WordDictionary()
    {
        root = new LetterNode();
    }

    public void AddWord(string word)
    {
        LetterNode currentNode = root;
        foreach (char c in word)
        {
            int index = c - 'a';
            if (currentNode.Alphabet[index] == null)
            {
                currentNode.Alphabet[index] = new LetterNode();
            }
            currentNode = currentNode.Alphabet[index];
        }
        currentNode.IsEnd = true;
    }

    public bool Search(string word)
    {
        return Dfs(word, root);
    }

    private bool Dfs(string target, LetterNode currentRoot)
    {
        if (target.Length == 0)
        {
            return currentRoot.IsEnd;
        }

        char firstLetter = target[0];
        string remainingTarget = target.Substring(1);

        if (firstLetter == '.')
        {
            for (int i = 0; i < 26; i++)
            {
                if (currentRoot.Alphabet[i] != null && Dfs(remainingTarget, currentRoot.Alphabet[i]))
                {
                    return true;
                }
            }
        }
        else
        {
            int index = firstLetter - 'a';
            if (currentRoot.Alphabet[index] != null)
            {
                return Dfs(remainingTarget, currentRoot.Alphabet[index]);
            }
        }

        return false;
    }
}
