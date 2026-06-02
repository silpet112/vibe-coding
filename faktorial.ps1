# faktorial.ps1
# Program, ktory vypocita faktorial cisla.
# Faktorial cisla n = 1 * 2 * 3 * ... * n   (napr. 5! = 1*2*3*4*5 = 120)

# --- Funkcia: "recept", ktory vypocita faktorial zadaneho cisla $n ---
function Faktorial {
    param([int]$n)

    # Faktorial zaporneho cisla nie je definovany -> vratime nic
    if ($n -lt 0) {
        return $null
    }

    # Zacneme od 1 a postupne nasobime az po $n.
    # [bigint] = velke cislo, aby fungovali aj velke faktorialy.
    $vysledok = [bigint]1
    for ($i = 2; $i -le $n; $i++) {
        $vysledok = $vysledok * $i
    }
    return $vysledok
}

# --- TU si nastav cislo, ktoreho faktorial chces vypocitat ---
$cislo = 6
Write-Output "Faktorial cisla $cislo je: $(Faktorial $cislo)"

# --- Automaticke overenie: program sa SAM skontroluje na znamych hodnotach ---
Write-Output ""
Write-Output "Overenie znamych hodnot:"

$testy = @(
    @{ vstup = 0;  ocakavane = 1 }
    @{ vstup = 1;  ocakavane = 1 }
    @{ vstup = 5;  ocakavane = 120 }
    @{ vstup = 10; ocakavane = 3628800 }
)

foreach ($t in $testy) {
    $vypocitane = Faktorial $t.vstup
    if ($vypocitane -eq [bigint]$t.ocakavane) {
        Write-Output "  [OK]    $($t.vstup)! = $vypocitane"
    } else {
        Write-Output "  [CHYBA] $($t.vstup)! = $vypocitane (ocakavane $($t.ocakavane))"
    }
}
