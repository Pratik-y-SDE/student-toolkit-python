def run():
    while True:
        print("\n+------------------------------+")
        print("|          QUIZ APP            |")
        print("+------------------------------+")
        print("|  1. Python                   |")
        print("|  2. Data Structures          |")
        print("|  3. General CS               |")
        print("|  4. Random Mixed Quiz        |")
        print("|  5. Back to Main Menu        |")
        print("+------------------------------+", flush=True)

        choice = input("\n  Enter choice (1-5): ").strip()

        if choice in ('1', '2', '3'):
            topic_map = {'1': 'Python', '2': 'Data Structures', '3': 'General CS'}
            topic     = topic_map[choice]
            questions = QUESTIONS[topic].copy()
            random.shuffle(questions)
            timed     = input("\n  Enable timed mode? (y/n): ").strip().lower() == 'y'
            run_quiz(topic, questions, timed)

        elif choice == '4':
            all_qs = []
            for t, qs in QUESTIONS.items():
                for q in qs:
                    # Store topic separately, do NOT pollute question dict
                    all_qs.append(dict(q))   # clean copy, no _topic key
            random.shuffle(all_qs)
            selected = all_qs[:min(10, len(all_qs))]
            timed    = input("\n  Enable timed mode? (y/n): ").strip().lower() == 'y'
            run_quiz("Mixed (Random)", selected, timed)

        elif choice == '5':
            break
        else:
            print("  [!] Invalid choice. Enter 1-5.", flush=True)
