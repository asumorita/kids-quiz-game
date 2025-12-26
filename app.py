import streamlit as st
import random

# ページ設定
st.set_page_config(
    page_title="クイズゲーム",
    page_icon="🎯",
    layout="centered"
)

# クイズデータ
QUIZZES = [
    # 動物クイズ
    {
        "question": "🐶 ワンワンと鳴く動物はどれ？",
        "options": ["ネコ", "イヌ", "ウサギ", "ライオン"],
        "answer": "イヌ",
        "emoji": "🐶"
    },
    {
        "question": "🐱 ニャーニャーと鳴く動物はどれ？",
        "options": ["イヌ", "ネコ", "トラ", "ゾウ"],
        "answer": "ネコ",
        "emoji": "🐱"
    },
    {
        "question": "🐘 鼻がとっても長い動物はどれ？",
        "options": ["キリン", "ゾウ", "サル", "ライオン"],
        "answer": "ゾウ",
        "emoji": "🐘"
    },
    {
        "question": "🦒 首がとっても長い動物はどれ？",
        "options": ["キリン", "ウマ", "シマウマ", "カバ"],
        "answer": "キリン",
        "emoji": "🦒"
    },
    {
        "question": "🐰 耳が長くてジャンプが得意な動物はどれ？",
        "options": ["イヌ", "ネコ", "ウサギ", "ネズミ"],
        "answer": "ウサギ",
        "emoji": "🐰"
    },
    # 食べ物クイズ
    {
        "question": "🍎 赤くて丸い果物はどれ？",
        "options": ["バナナ", "リンゴ", "ブドウ", "ミカン"],
        "answer": "リンゴ",
        "emoji": "🍎"
    },
    {
        "question": "🍌 黄色くて細長い果物はどれ？",
        "options": ["バナナ", "リンゴ", "イチゴ", "スイカ"],
        "answer": "バナナ",
        "emoji": "🍌"
    },
    {
        "question": "🍓 赤くて小さくて甘い果物はどれ？",
        "options": ["リンゴ", "イチゴ", "トマト", "サクランボ"],
        "answer": "イチゴ",
        "emoji": "🍓"
    },
    {
        "question": "🍚 日本人が毎日食べる白い食べ物はどれ？",
        "options": ["パン", "ごはん", "麺", "ケーキ"],
        "answer": "ごはん",
        "emoji": "🍚"
    },
    {
        "question": "🍕 丸くてチーズがのってる食べ物はどれ？",
        "options": ["ハンバーガー", "ピザ", "ホットドッグ", "サンドイッチ"],
        "answer": "ピザ",
        "emoji": "🍕"
    },
    # 色クイズ
    {
        "question": "🌈 空の色は何色？",
        "options": ["赤", "青", "黄色", "緑"],
        "answer": "青",
        "emoji": "☁️"
    },
    {
        "question": "🌸 桜の花の色は何色？",
        "options": ["ピンク", "赤", "青", "黄色"],
        "answer": "ピンク",
        "emoji": "🌸"
    },
    {
        "question": "🍋 レモンの色は何色？",
        "options": ["赤", "青", "黄色", "緑"],
        "answer": "黄色",
        "emoji": "🍋"
    },
    {
        "question": "🍅 トマトの色は何色？",
        "options": ["赤", "青", "黄色", "緑"],
        "answer": "赤",
        "emoji": "🍅"
    },
    # その他
    {
        "question": "⭐ 夜に空でキラキラ光るものは何？",
        "options": ["太陽", "星", "月", "雲"],
        "answer": "星",
        "emoji": "⭐"
    },
]

# セッション状態の初期化
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.current_quiz_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected_answer = None
    st.session_state.quiz_list = []

# タイトル
st.title("🎯 クイズゲーム")
st.write("全部で何問正解できるかな？")

# ゲーム開始前
if not st.session_state.quiz_started:
    st.markdown("---")
    
    st.subheader("✨ ルール説明")
    st.write("📝 問題が出るよ")
    st.write("🎯 4つの中から正しい答えを選んでね")
    st.write("⭐ 正解すると1点もらえるよ")
    st.write("🎉 全部で15問あるよ！")
    
    st.markdown("---")
    
    # 問題数を選択
    num_questions = st.slider(
        "何問挑戦する？",
        min_value=5,
        max_value=15,
        value=10,
        step=1
    )
    
    if st.button("🎮 ゲームスタート！", type="primary", use_container_width=True):
        # ランダムに問題を選ぶ
        st.session_state.quiz_list = random.sample(QUIZZES, num_questions)
        st.session_state.quiz_started = True
        st.session_state.current_quiz_index = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()

# ゲーム中
else:
    # 現在の問題
    current_index = st.session_state.current_quiz_index
    total_questions = len(st.session_state.quiz_list)
    
    # ゲーム終了判定
    if current_index >= total_questions:
        st.markdown("---")
        st.success("🎉 クイズ終了！")
        
        score = st.session_state.score
        total = total_questions
        percentage = (score / total) * 100
        
        # 結果表示
        st.markdown(f"### あなたのスコア: {score}点 / {total}問")
        st.progress(score / total)
        
        # 評価
        if percentage == 100:
            st.balloons()
            st.success("🏆 パーフェクト！全問正解だよ！すごすぎる！！")
        elif percentage >= 80:
            st.success("🌟 すごい！よくできました！")
        elif percentage >= 60:
            st.info("👍 いい感じ！がんばったね！")
        elif percentage >= 40:
            st.info("😊 まずまず！次はもっと取れるよ！")
        else:
            st.info("💪 もう一回チャレンジしてみよう！")
        
        st.markdown("---")
        
        if st.button("🔄 もう一回遊ぶ", type="primary", use_container_width=True):
            st.session_state.quiz_started = False
            st.rerun()
    
    else:
        # 進捗表示
        st.progress((current_index + 1) / total_questions)
        st.write(f"問題 {current_index + 1} / {total_questions}")
        
        # スコア表示
        col1, col2 = st.columns(2)
        with col1:
            st.metric("⭐ 現在のスコア", f"{st.session_state.score}点")
        with col2:
            st.metric("❓ 残り問題", f"{total_questions - current_index - 1}問")
        
        st.markdown("---")
        
        # 問題表示
        quiz = st.session_state.quiz_list[current_index]
        
        st.subheader(quiz["question"])
        
        # 答えが選ばれていない場合
        if not st.session_state.answered:
            # 選択肢をシャッフル
            if 'shuffled_options' not in st.session_state:
                st.session_state.shuffled_options = quiz["options"].copy()
                random.shuffle(st.session_state.shuffled_options)
            
            # ボタンで選択肢を表示
            for option in st.session_state.shuffled_options:
                if st.button(option, key=f"option_{option}", use_container_width=True):
                    st.session_state.selected_answer = option
                    st.session_state.answered = True
                    
                    # 正解判定
                    if option == quiz["answer"]:
                        st.session_state.score += 1
                    
                    st.rerun()
        
        # 答えた後
        else:
            selected = st.session_state.selected_answer
            correct = quiz["answer"]
            
            # 結果表示
            if selected == correct:
                st.success(f"🎉 正解！ {quiz['emoji']} すごいね！")
            else:
                st.error(f"❌ 残念！正解は「{correct}」だよ")
                st.info("次はがんばろう！")
            
            st.markdown("---")
            
            # 次の問題へ
            if st.button("➡️ 次の問題へ", type="primary", use_container_width=True):
                st.session_state.current_quiz_index += 1
                st.session_state.answered = False
                st.session_state.selected_answer = None
                if 'shuffled_options' in st.session_state:
                    del st.session_state.shuffled_options
                st.rerun()

# フッター
st.markdown("---")
st.caption("💡 家族みんなで挑戦してみてね！")
st.caption("Created with ❤️ for パパの娘ちゃん")
