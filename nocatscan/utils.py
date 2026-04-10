def save_results(results, filename):
    with open(filename, "w") as f:
        for port, banner in results:
            f.write(f"{port} | {banner}\n")

    print(f"\n[+] Hasil disimpan ke {filename}")