# Automated Tests

_The contents of the file below the following line were generated using_
`./manage.py test > docs/automated-tests.md -v 2 2>&1`

_Lines were modified with a find and replace all search for `(.)\n` and
replacing with `$1  \n`_

---

Found 83 test(s).  
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  

Operations to perform:  
  Synchronize unmigrated apps: allauth, cloudinary, cloudinary_storage, corsheaders, dj_rest_auth, django_filters, messages, registration, rest_framework, staticfiles  
  Apply all migrations: account, admin, auth, authtoken, contenttypes, dice, games, moves, profiles, sessions, sites, socialaccount, winners  
Synchronizing apps without migrations:  
  Creating tables...  
    Running deferred SQL...  
Running migrations:  
  Applying contenttypes.0001_initial... OK  
  Applying auth.0001_initial... OK  
  Applying account.0001_initial... OK  
  Applying account.0002_email_max_length... OK  
  Applying admin.0001_initial... OK  
  Applying admin.0002_logentry_remove_auto_add... OK  
  Applying admin.0003_logentry_add_action_flag_choices... OK  
  Applying contenttypes.0002_remove_content_type_name... OK  
  Applying auth.0002_alter_permission_name_max_length... OK  
  Applying auth.0003_alter_user_email_max_length... OK  
  Applying auth.0004_alter_user_username_opts... OK  
  Applying auth.0005_alter_user_last_login_null... OK  
  Applying auth.0006_require_contenttypes_0002... OK  
  Applying auth.0007_alter_validators_add_error_messages... OK  
  Applying auth.0008_alter_user_username_max_length... OK  
  Applying auth.0009_alter_user_last_name_max_length... OK  
  Applying auth.0010_alter_group_name_max_length... OK  
  Applying auth.0011_update_proxy_permissions... OK  
  Applying auth.0012_alter_user_first_name_max_length... OK  
  Applying authtoken.0001_initial... OK  
  Applying authtoken.0002_auto_20160226_1747... OK  
  Applying authtoken.0003_tokenproxy... OK  
  Applying authtoken.0004_alter_tokenproxy_options... OK  
  Applying winners.0001_initial... OK  
  Applying games.0001_initial... OK  
  Applying games.0002_alter_game_winner... OK  
  Applying games.0003_alter_game_winner... OK  
  Applying dice.0001_initial... OK  
  Applying dice.0002_rename_value_die_value1_die_value2... OK  
  Applying dice.0003_rename_die_diceroll... OK  
  Applying dice.0004_alter_diceroll_options_diceroll_created_at_and_more... OK  
  Applying games.0004_remove_game_winner... OK  
  Applying moves.0001_initial... OK  
  Applying moves.0002_alter_move_game_alter_move_owner... OK  
  Applying profiles.0001_initial... OK  
  Applying sessions.0001_initial... OK  
  Applying sites.0001_initial... OK  
  Applying sites.0002_alter_domain_unique... OK  
  Applying socialaccount.0001_initial... OK  
  Applying socialaccount.0002_token_max_lengths... OK  
  Applying socialaccount.0003_extra_data_default_dict... OK  
  Applying winners.0002_winner_game_alter_winner_owner... OK  
System check identified no issues (1 silenced).  
test_dice_roll_cannot_be_set_by_user (dice.tests.DiceRollListViewTests.test_dice_roll_cannot_be_set_by_user) ... ok  
test_dice_roll_is_random_value_1_to_6 (dice.tests.DiceRollListViewTests.test_dice_roll_is_random_value_1_to_6) ... ok  
test_logged_in_user_can_create_dice_roll_in_their_game (dice.tests.DiceRollListViewTests.test_logged_in_user_can_create_dice_roll_in_their_game) ... ok  
test_logged_in_user_can_list_dice_rolls (dice.tests.DiceRollListViewTests.test_logged_in_user_can_list_dice_rolls) ... ok  
test_logged_in_user_can_only_create_dice_roll_on_their_turn (dice.tests.DiceRollListViewTests.test_logged_in_user_can_only_create_dice_roll_on_their_turn) ... ok  
test_logged_in_user_cannot_create_dice_roll_in_non_existent_game (dice.tests.DiceRollListViewTests.test_logged_in_user_cannot_create_dice_roll_in_non_existent_game) ... ok  
test_logged_in_user_cannot_create_dice_roll_in_other_game (dice.tests.DiceRollListViewTests.test_logged_in_user_cannot_create_dice_roll_in_other_game) ... ok  
test_logged_in_user_cannot_delete_dice_roll (dice.tests.DiceRollListViewTests.test_logged_in_user_cannot_delete_dice_roll) ... ok  
test_logged_in_user_cannot_update_dice_roll (dice.tests.DiceRollListViewTests.test_logged_in_user_cannot_update_dice_roll) ... ok  
test_logged_out_user_can_view_dice_rolls (dice.tests.DiceRollListViewTests.test_logged_out_user_can_view_dice_rolls) ... ok  
test_logged_out_user_cannot_create_dice_roll (dice.tests.DiceRollListViewTests.test_logged_out_user_cannot_create_dice_roll) ... ok  
test_game_players_cannot_be_changed (games.tests.GameDetailViewTests.test_game_players_cannot_be_changed) ... ok  
test_logged_in_user_can_update_owned_game (games.tests.GameDetailViewTests.test_logged_in_user_can_update_owned_game) ... ok  
test_logged_in_user_can_view_specific_game (games.tests.GameDetailViewTests.test_logged_in_user_can_view_specific_game) ... ok  
test_logged_in_user_cannot_delete_other_players_game (games.tests.GameDetailViewTests.test_logged_in_user_cannot_delete_other_players_game) ... ok  
test_logged_in_user_cannot_delete_owned_game (games.tests.GameDetailViewTests.test_logged_in_user_cannot_delete_owned_game) ... ok  
test_logged_in_user_cannot_update_other_players_game (games.tests.GameDetailViewTests.test_logged_in_user_cannot_update_other_players_game) ... ok  
test_logged_in_user_cannot_view_non_existent_game (games.tests.GameDetailViewTests.test_logged_in_user_cannot_view_non_existent_game) ... ok  
test_logged_out_user_can_view_specific_game (games.tests.GameDetailViewTests.test_logged_out_user_can_view_specific_game) ... ok  
test_logged_out_user_cannot_delete_game (games.tests.GameDetailViewTests.test_logged_out_user_cannot_delete_game) ... ok  
test_logged_out_user_cannot_update_game (games.tests.GameDetailViewTests.test_logged_out_user_cannot_update_game) ... ok  
test_logged_out_user_cannot_view_non_existent_game (games.tests.GameDetailViewTests.test_logged_out_user_cannot_view_non_existent_game) ... ok  
test_active_filter_works_as_expected (games.tests.GameListViewTests.test_active_filter_works_as_expected) ... ok  
test_can_list_games (games.tests.GameListViewTests.test_can_list_games) ... ok  
test_either_player_filter_works_as_expected (games.tests.GameListViewTests.test_either_player_filter_works_as_expected) ... ok  
test_game_count_reflects_number_of_games (games.tests.GameListViewTests.test_game_count_reflects_number_of_games) ... ok  
test_logged_in_user_can_create_game (games.tests.GameListViewTests.test_logged_in_user_can_create_game) ... ok  
test_logged_in_user_cannot_create_game_against_themself (games.tests.GameListViewTests.test_logged_in_user_cannot_create_game_against_themself) ... ok  
test_logged_in_user_cannot_create_game_with_nonexistent_player (games.tests.GameListViewTests.test_logged_in_user_cannot_create_game_with_nonexistent_player) ... ok  
test_logged_in_user_cannot_create_game_without_self_as_a_player (games.tests.GameListViewTests.test_logged_in_user_cannot_create_game_without_self_as_a_player) ... ok  
test_logged_in_user_is_not_player_1_in_appropriate_game (games.tests.GameListViewTests.test_logged_in_user_is_not_player_1_in_appropriate_game) ... ok  
test_logged_in_user_is_not_player_2_in_appropriate_game (games.tests.GameListViewTests.test_logged_in_user_is_not_player_2_in_appropriate_game) ... ok  
test_logged_in_user_is_player_1_in_appropriate_game (games.tests.GameListViewTests.test_logged_in_user_is_player_1_in_appropriate_game) ... ok  
test_logged_in_user_is_player_2_in_appropriate_game (games.tests.GameListViewTests.test_logged_in_user_is_player_2_in_appropriate_game) ... ok  
test_logged_out_user_cannot_create_game (games.tests.GameListViewTests.test_logged_out_user_cannot_create_game) ... ok  
test_new_game_has_default_image (games.tests.GameListViewTests.test_new_game_has_default_image) ... ok  
test_new_game_is_active (games.tests.GameListViewTests.test_new_game_is_active) ... ok  
test_player_1_filter_works_as_expected (games.tests.GameListViewTests.test_player_1_filter_works_as_expected) ... ok  
test_player_2_filter_works_as_expected (games.tests.GameListViewTests.test_player_2_filter_works_as_expected) ... ok  
test_logged_in_user_can_delete_owned_move (moves.tests.MoveDetailViewTests.test_logged_in_user_can_delete_owned_move) ... ok  
test_logged_in_user_can_update_owned_move (moves.tests.MoveDetailViewTests.test_logged_in_user_can_update_owned_move) ... ok  
test_logged_in_user_can_view_specific_move (moves.tests.MoveDetailViewTests.test_logged_in_user_can_view_specific_move) ... ok  
test_logged_in_user_cannot_delete_move_that_is_not_latest (moves.tests.MoveDetailViewTests.test_logged_in_user_cannot_delete_move_that_is_not_latest) ... ok  
test_logged_in_user_cannot_update_move_that_is_not_latest (moves.tests.MoveDetailViewTests.test_logged_in_user_cannot_update_move_that_is_not_latest) ... ok  
test_logged_in_user_cannot_update_other_move (moves.tests.MoveDetailViewTests.test_logged_in_user_cannot_update_other_move) ... ok  
test_logged_in_user_cannot_view_non_existent_move (moves.tests.MoveDetailViewTests.test_logged_in_user_cannot_view_non_existent_move) ... ok  
test_logged_out_user_can_view_specific_move (moves.tests.MoveDetailViewTests.test_logged_out_user_can_view_specific_move) ... ok  
test_logged_out_user_cannot_delete_move (moves.tests.MoveDetailViewTests.test_logged_out_user_cannot_delete_move) ... ok  
test_logged_out_user_cannot_update_move (moves.tests.MoveDetailViewTests.test_logged_out_user_cannot_update_move) ... ok  
test_logged_out_user_cannot_view_non_existent_move (moves.tests.MoveDetailViewTests.test_logged_out_user_cannot_view_non_existent_move) ... ok  
test_can_list_moves (moves.tests.MoveListViewTests.test_can_list_moves) ... ok  
test_game_filter_works_as_expected (moves.tests.MoveListViewTests.test_game_filter_works_as_expected) ... ok  
test_logged_in_user_can_create_move (moves.tests.MoveListViewTests.test_logged_in_user_can_create_move) ... ok  
test_logged_in_user_can_create_move_with_content (moves.tests.MoveListViewTests.test_logged_in_user_can_create_move_with_content) ... ok  
test_logged_in_user_cannot_create_move_in_other_game (moves.tests.MoveListViewTests.test_logged_in_user_cannot_create_move_in_other_game) ... ok  
test_logged_out_user_cannot_create_move (moves.tests.MoveListViewTests.test_logged_out_user_cannot_create_move) ... ok  
test_player_filter_works_as_expected (moves.tests.MoveListViewTests.test_player_filter_works_as_expected) ... ok  
test_logged_in_user_can_update_owned_profile (profiles.tests.ProfileDetailViewTests.test_logged_in_user_can_update_owned_profile) ... ok  
test_logged_in_user_can_view_specific_profile (profiles.tests.ProfileDetailViewTests.test_logged_in_user_can_view_specific_profile) ... ok  
test_logged_in_user_cannot_delete_other_profile (profiles.tests.ProfileDetailViewTests.test_logged_in_user_cannot_delete_other_profile) ... ok  
test_logged_in_user_cannot_delete_owned_profile (profiles.tests.ProfileDetailViewTests.test_logged_in_user_cannot_delete_owned_profile) ... ok  
test_logged_in_user_cannot_update_other_profile (profiles.tests.ProfileDetailViewTests.test_logged_in_user_cannot_update_other_profile) ... ok  
test_logged_in_user_cannot_view_non_existent_profile (profiles.tests.ProfileDetailViewTests.test_logged_in_user_cannot_view_non_existent_profile) ... ok  
test_logged_out_user_can_view_specific_profile (profiles.tests.ProfileDetailViewTests.test_logged_out_user_can_view_specific_profile) ... ok  
test_logged_out_user_cannot_delete_profile (profiles.tests.ProfileDetailViewTests.test_logged_out_user_cannot_delete_profile) ... ok  
test_logged_out_user_cannot_update_profile (profiles.tests.ProfileDetailViewTests.test_logged_out_user_cannot_update_profile) ... ok  
test_logged_out_user_cannot_view_non_existent_profile (profiles.tests.ProfileDetailViewTests.test_logged_out_user_cannot_view_non_existent_profile) ... ok  
test_can_list_profiles (profiles.tests.ProfileListViewTests.test_can_list_profiles) ... ok  
test_cannot_create_profile (profiles.tests.ProfileListViewTests.test_cannot_create_profile) ... ok  
test_logged_in_user_is_not_other_profile_owner (profiles.tests.ProfileListViewTests.test_logged_in_user_is_not_other_profile_owner) ... ok  
test_logged_in_user_is_profile_owner (profiles.tests.ProfileListViewTests.test_logged_in_user_is_profile_owner) ... ok  
test_logged_out_user_is_not_a_profile_owner (profiles.tests.ProfileListViewTests.test_logged_out_user_is_not_a_profile_owner) ... ok  
test_new_profile_has_default_image (profiles.tests.ProfileListViewTests.test_new_profile_has_default_image) ... ok  
test_profile_count_reflects_number_of_profiles (profiles.tests.ProfileListViewTests.test_profile_count_reflects_number_of_profiles) ... ok  
test_logged_in_user_can_create_winners_in_their_game (winners.tests.WinnerListViewTests.test_logged_in_user_can_create_winners_in_their_game) ... ok  
test_logged_in_user_can_list_winners (winners.tests.WinnerListViewTests.test_logged_in_user_can_list_winners) ... ok  
test_logged_in_user_cannot_create_winner_on_game_with_winner (winners.tests.WinnerListViewTests.test_logged_in_user_cannot_create_winner_on_game_with_winner) ... ok  
test_logged_in_user_cannot_create_winners_in_non_existent_game (winners.tests.WinnerListViewTests.test_logged_in_user_cannot_create_winners_in_non_existent_game) ... ok  
test_logged_in_user_cannot_create_winners_in_other_game (winners.tests.WinnerListViewTests.test_logged_in_user_cannot_create_winners_in_other_game) ... ok  
test_logged_in_user_cannot_delete_winners (winners.tests.WinnerListViewTests.test_logged_in_user_cannot_delete_winners) ... ok  
test_logged_in_user_cannot_update_winners (winners.tests.WinnerListViewTests.test_logged_in_user_cannot_update_winners) ... ok  
test_logged_out_user_can_view_winners (winners.tests.WinnerListViewTests.test_logged_out_user_can_view_winners) ... ok  
test_logged_out_user_cannot_create_winners (winners.tests.WinnerListViewTests.test_logged_out_user_cannot_create_winners) ... ok  

----------------------------------------------------------------------  
Ran 83 tests in 79.896s  

OK  
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...  
