# TestCollegamento
TestDiCollegamento

## Come eliminare l'avviso "Apply changes and continue locally?"
Se l'IDE mostra il banner

```
Apply changes and continue locally? This task was made in <repo> so may not apply cleanly.
```

significa che stai provando ad applicare una patch generata per un altro repository.
Per chiudere l'avviso e continuare a lavorare su questo progetto:

1. Annulla l'operazione di applicazione della patch cliccando su **Cancel/Don't apply** o premendo `Esc`.
2. Assicurati di avere aperto localmente la cartella corretta (`TestCollegamento`) e di non applicare patch create per percorsi diversi.
3. Se il messaggio riappare, ripeti il comando locale senza usare la patch remota oppure copia i cambiamenti a mano nel tuo editor.

In questo modo l'avviso scompare e lavori solo con i file presenti in questa copia del repository.
